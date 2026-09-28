"""Upload a sliced 3MF from the job card, match its materials, and print it.

The Creator 5 series does not report which tools a stored file uses, so the
only way to map its tools to Material Station slots correctly is to read the
3MF before it reaches the printer. This module is that path, and it serves the
AD5X and the 5M series too:

1. **Stage** - the card POSTs the file to :class:`FlashForgeUploadView`. The
   bytes stream to a scratch file (never into memory), capped at
   :data:`MAX_UPLOAD_BYTES`, and ``flashforge.threemf.parse_3mf`` reads the
   tools and materials. The response has the same shape as ``job/prepare``, so
   the card reuses its matching dialog.
2. **Start** - ``flashforge/upload/start`` re-validates the mapping against the
   live station report (the card is untrusted, exactly as for local starts),
   then sends the file with the per-model upload command.
3. **Discard** - ``flashforge/upload/discard``, or the TTL, deletes the scratch
   file when the user closes the dialog or walks away.

Per-model dispatch mirrors FlashForgeUI and the standalone WebUI:

* **Creator 5 / 5 Pro** - upload without starting, then ``start_creator5_job``
  with a mapping for every tool. A Material Station and per-tool data are
  required: without mappings the firmware prints each tool from the slot with
  the slicer's filament number, whatever is loaded there.
* **AD5X** - ``upload_file_ad5x`` with the mappings, starting at once. With no
  station reported, a plain upload that prints from the external spool.
* **5M / 5M Pro** - a plain upload that starts at once. No matching.
"""
from __future__ import annotations

import asyncio
import base64
import logging
import shutil
import tempfile
import time
import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, BinaryIO

import voluptuous as vol
from flashforge import FlashForgeClient
from flashforge.models import (
    AD5XMaterialMapping,
    AD5XUploadParams,
    Creator5JobParams,
    Creator5UploadParams,
    FFMachineInfo,
)
from flashforge.threemf import PrinterFamily, ThreeMFError, ThreeMFFile, parse_3mf

from homeassistant.components import websocket_api
from homeassistant.components.http import HomeAssistantView
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN
from .job import (
    MAX_SLOTS,
    JobStartError,
    auto_match,
    color_warnings,
    slots_to_list,
    validate_mappings,
)
from .util import is_creator5_series

_LOGGER = logging.getLogger(__name__)

MAX_UPLOAD_BYTES = 500 * 1024 * 1024
"""Largest file the card may upload. Guards the disk of a small host."""

STAGE_TTL_SECONDS = 30 * 60
"""A staged file is deleted this long after upload if nobody starts it."""

MAX_STAGED_UPLOADS = 8
"""Upper bound on files waiting at once, across all printers."""

CHUNK_BYTES = 1024 * 1024

STAGE_DIR_NAME = "flashforge-hass-uploads"

_STORE_KEY = f"{DOMAIN}_upload_store"

# States in which the printer cannot take a new job. Sending hundreds of
# megabytes only for the printer to refuse the start is worth avoiding, so the
# start command checks first. The printer still has the final word.
BUSY_STATES = frozenset(
    {"printing", "pausing", "paused", "heating", "calibrating", "busy"}
)

PLAN_CREATOR5 = "creator5"
PLAN_AD5X_STATION = "ad5x_station"
PLAN_PLAIN = "plain"

ERR_UPLOAD_NOT_FOUND = "upload_not_found"
ERR_PRINTER = "printer_error"
ERR_ENTRY_NOT_FOUND = "entry_not_found"

MATERIAL_MAPPING_SCHEMA = vol.Schema(
    {vol.Required("tool_id"): int, vol.Required("slot_id"): int},
    # Material names and colors are re-derived server-side; see websocket.py.
    extra=vol.ALLOW_EXTRA,
)


class UploadError(HomeAssistantError):
    """The uploaded file cannot be staged or printed. Carries an HTTP status."""

    def __init__(self, message: str, status: int = 400) -> None:
        super().__init__(message)
        self.status = status


# --------------------------------------------------------------------------- #
# Pure helpers
# --------------------------------------------------------------------------- #


def sanitize_file_name(name: str | None) -> str | None:
    """Return a safe bare ``.3mf`` file name, or None to refuse the upload.

    Path separators are refused outright rather than stripped, so a traversal
    attempt fails instead of succeeding under a new name. The printer stores the
    file under this name, so it is otherwise kept verbatim.
    """
    if not name or len(name) > 255:
        return None
    if "/" in name or "\\" in name or "\0" in name or name.startswith("."):
        return None
    if not name.lower().endswith(".3mf"):
        return None
    return name


def printer_family(machine_info: FFMachineInfo | None) -> PrinterFamily:
    """The connected printer's family, from the library's PID-derived flags."""
    if getattr(machine_info, "is_creator5_pro", False):
        return PrinterFamily.CREATOR_5_PRO
    if getattr(machine_info, "is_creator5", False):
        return PrinterFamily.CREATOR_5
    if getattr(machine_info, "is_ad5x", False):
        return PrinterFamily.AD5X
    if getattr(machine_info, "is_pro", False):
        return PrinterFamily.ADVENTURER_5M_PRO
    return PrinterFamily.ADVENTURER_5M


def model_mismatch(info: ThreeMFFile, machine_info: FFMachineInfo | None) -> str | None:
    """Return the file's printer model id when it was sliced for another model.

    A warning, never a refusal: slicers disagree on model ids, and an unknown
    id says nothing either way.
    """
    sliced_for = info.printer_family
    if sliced_for is None or sliced_for == printer_family(machine_info):
        return None
    return info.printer_model_id


def threemf_to_file_entry(info: ThreeMFFile) -> dict[str, Any]:
    """Describe a parsed 3MF in the shape ``job.file_to_dict`` produces.

    The matching rules in job.py work on this shape, so an uploaded file goes
    through exactly the checks a file listed by the printer does.
    """
    return {
        "file_name": info.file_name,
        "printing_time": info.estimated_time_s,
        "total_filament_weight": info.total_weight_g,
        "tool_count": info.tool_count,
        # The card warns when a station file meets a printer with no station.
        # A 3MF does not record whether it was sliced for one, so only a
        # multi-filament file counts: one filament prints fine from a spool.
        "use_matl_station": info.tool_count > 1,
        "tool_datas": [
            {
                "tool_id": filament.tool_id,
                "material_name": filament.material_name,
                "material_color": filament.color,
                "filament_weight": filament.used_g or 0.0,
                # No slicer slot hint in a 3MF; auto_match picks by material.
                "slot_id": 0,
            }
            for filament in info.filaments
        ],
    }


def upload_plan(
    machine_info: FFMachineInfo | None,
    slots: list[dict[str, Any]],
    file_entry: dict[str, Any],
) -> str:
    """Pick the upload path for this printer and file, or explain why not.

    Raises:
        UploadError: If the file cannot be printed correctly on this printer.
    """
    tools = file_entry.get("tool_datas") or []

    if is_creator5_series(machine_info):
        plan = PLAN_CREATOR5
        if not slots:
            raise UploadError(
                "The printer is not reporting its Material Station, so the tools in "
                "this file cannot be matched to slots. Check the station and try again."
            )
    elif getattr(machine_info, "is_ad5x", False) and slots:
        plan = PLAN_AD5X_STATION
    else:
        return PLAN_PLAIN

    if not tools:
        raise UploadError(
            f"'{file_entry['file_name']}' does not say which filaments it uses, so its "
            "tools cannot be matched to Material Station slots. Re-slice it and export "
            "the sliced plate again."
        )
    too_high = [tool["tool_id"] + 1 for tool in tools if tool["tool_id"] >= MAX_SLOTS]
    if too_high:
        raise UploadError(
            f"'{file_entry['file_name']}' uses filament {too_high[0]}, but the Material "
            f"Station has {MAX_SLOTS} slots. Re-slice it with filaments 1 to {MAX_SLOTS}."
        )
    return plan


def plan_requires_matching(plan: str) -> bool:
    """Return True when this upload path needs a mapping for every tool."""
    return plan in (PLAN_CREATOR5, PLAN_AD5X_STATION)


# --------------------------------------------------------------------------- #
# Staging
# --------------------------------------------------------------------------- #


@dataclass
class StagedUpload:
    """A parsed 3MF waiting on disk for the user to start it."""

    upload_id: str
    entry_id: str
    path: Path
    info: ThreeMFFile
    file_entry: dict[str, Any]
    created: float = field(default_factory=time.monotonic)
    in_progress: bool = False
    expiry: asyncio.TimerHandle | None = None

    @property
    def file_name(self) -> str:
        return self.path.name


class UploadStore:
    """Scratch files for uploads, by opaque id, with a TTL.

    Each upload gets its own directory so the original file name can be kept
    verbatim: the printer stores the file under the name it is sent.
    """

    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self._staged: dict[str, StagedUpload] = {}
        self._cleaned_orphans = False

    def __len__(self) -> int:
        return len(self._staged)

    def get(self, upload_id: str, entry_id: str) -> StagedUpload | None:
        """Return the staged upload, but only for the printer it was staged for."""
        staged = self._staged.get(upload_id)
        if staged is None or staged.entry_id != entry_id:
            return None
        return staged

    def add(self, staged: StagedUpload) -> None:
        self._staged[staged.upload_id] = staged

    def pop(self, upload_id: str) -> StagedUpload | None:
        staged = self._staged.pop(upload_id, None)
        if staged is not None and staged.expiry is not None:
            staged.expiry.cancel()
        return staged

    def expired(self, now: float | None = None) -> list[str]:
        """Ids past the TTL that are not being sent right now."""
        now = time.monotonic() if now is None else now
        return [
            upload_id
            for upload_id, staged in self._staged.items()
            if not staged.in_progress and now - staged.created >= STAGE_TTL_SECONDS
        ]

    def take_orphan_cleanup(self) -> bool:
        """True exactly once: the first upload of a run clears old scratch files."""
        if self._cleaned_orphans:
            return False
        self._cleaned_orphans = True
        return True


def get_store(hass: HomeAssistant) -> UploadStore:
    """The upload store for this Home Assistant run."""
    store = hass.data.get(_STORE_KEY)
    if store is None:
        store = UploadStore(Path(tempfile.gettempdir()) / STAGE_DIR_NAME)
        hass.data[_STORE_KEY] = store
    return store


def _remove_tree(path: Path) -> None:
    shutil.rmtree(path, ignore_errors=True)


def _clear_directory(directory: Path) -> None:
    if directory.is_dir():
        for child in directory.iterdir():
            _remove_tree(child)


async def async_discard(hass: HomeAssistant, store: UploadStore, upload_id: str) -> None:
    """Forget a staged upload and delete its scratch directory."""
    staged = store.pop(upload_id)
    if staged is not None:
        await hass.async_add_executor_job(_remove_tree, staged.path.parent)


def _expire(hass: HomeAssistant, store: UploadStore, upload_id: str) -> None:
    """TTL callback. A file being sent right now is left alone and checked
    again in a minute: the start command deletes it when the send succeeds, and
    a failed send leaves it for this timer."""
    staged = store._staged.get(upload_id)
    if staged is None:
        return
    if staged.in_progress:
        staged.expiry = asyncio.get_running_loop().call_later(
            60, _expire, hass, store, upload_id
        )
        return
    hass.async_create_task(async_discard(hass, store, upload_id))


async def async_sweep(hass: HomeAssistant, store: UploadStore) -> None:
    """Delete every staged upload past its TTL."""
    for upload_id in store.expired():
        await async_discard(hass, store, upload_id)


def _open_for_write(path: Path) -> BinaryIO:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.open("wb")


async def async_stage_upload(
    hass: HomeAssistant,
    entry_id: str,
    file_name: str | None,
    chunks: AsyncIterator[bytes],
) -> dict[str, Any]:
    """Write an uploaded 3MF to scratch storage, parse it, and describe it.

    Returns:
        The card's dialog payload: the upload id, the file in ``job/prepare``
        shape, the slots, a suggested mapping, and any warnings.

    Raises:
        UploadError: If the printer is unknown, the file is refused, too large,
            not a printable 3MF, or cannot be matched on this printer.
    """
    data = hass.data.get(DOMAIN, {}).get(entry_id)
    if data is None:
        raise UploadError("That FlashForge printer is not set up.", status=404)

    name = sanitize_file_name(file_name)
    if name is None:
        raise UploadError("Only sliced .3mf files can be uploaded.")

    store = get_store(hass)
    if store.take_orphan_cleanup():
        # Scratch files left by a previous run (a crash, a restart mid-upload).
        await hass.async_add_executor_job(_clear_directory, store.directory)
    await async_sweep(hass, store)
    if len(store) >= MAX_STAGED_UPLOADS:
        raise UploadError(
            "Too many uploads are waiting to start. Start or close one, then try again.",
            status=429,
        )

    upload_id = uuid.uuid4().hex
    path = store.directory / upload_id / name
    size = 0
    handle = await hass.async_add_executor_job(_open_for_write, path)
    try:
        async for chunk in chunks:
            size += len(chunk)
            if size > MAX_UPLOAD_BYTES:
                raise UploadError(
                    f"The file is larger than {MAX_UPLOAD_BYTES // (1024 * 1024)} MB.",
                    status=413,
                )
            await hass.async_add_executor_job(handle.write, chunk)
    except BaseException:
        await hass.async_add_executor_job(handle.close)
        await hass.async_add_executor_job(_remove_tree, path.parent)
        raise
    await hass.async_add_executor_job(handle.close)

    try:
        if size == 0:
            raise UploadError("The uploaded file is empty.")
        try:
            info = await hass.async_add_executor_job(parse_3mf, path)
        except ThreeMFError as err:
            raise UploadError(str(err)) from err

        coordinator = data["coordinator"]
        machine_info = coordinator.data
        file_entry = threemf_to_file_entry(info)
        slots = slots_to_list(machine_info)
        plan = upload_plan(machine_info, slots, file_entry)
    except BaseException:
        await hass.async_add_executor_job(_remove_tree, path.parent)
        raise

    staged = StagedUpload(
        upload_id=upload_id,
        entry_id=entry_id,
        path=path,
        info=info,
        file_entry=file_entry,
    )
    store.add(staged)
    staged.expiry = asyncio.get_running_loop().call_later(
        STAGE_TTL_SECONDS, _expire, hass, store, upload_id
    )
    _LOGGER.debug(
        "Staged %s for %s (%d bytes, %d tools, plan=%s)",
        name,
        data.get("name"),
        size,
        info.tool_count,
        plan,
    )

    needs_matching = plan_requires_matching(plan)
    suggested = auto_match(file_entry, slots) if needs_matching else []
    return {
        "upload_id": upload_id,
        "file": file_entry,
        "slots": slots,
        "requires_matching": needs_matching,
        "suggested_mappings": suggested,
        "suggestion_complete": needs_matching
        and len(suggested) == len(file_entry["tool_datas"]),
        "thumbnail": base64.b64encode(info.thumbnail_png).decode("ascii")
        if info.thumbnail_png
        else None,
        "model_mismatch": model_mismatch(info, machine_info),
        "slicer_warnings": [warning.message for warning in info.warnings if warning.message],
    }


# --------------------------------------------------------------------------- #
# Dispatch
# --------------------------------------------------------------------------- #


async def async_upload_and_print(
    client: FlashForgeClient,
    plan: str,
    path: Path,
    *,
    leveling_before_print: bool,
    mappings: list[AD5XMaterialMapping],
) -> None:
    """Send a staged 3MF to the printer and start it.

    Raises:
        JobStartError: If the upload or the start fails.
    """
    file_name = path.name
    job_control = client.job_control

    try:
        if plan == PLAN_CREATOR5:
            # Two steps, as in FlashForgeUI: upload without starting, then start
            # with the mappings. The firmware keeps upload-time mappings until
            # the next print ends, so they are never sent on a non-starting upload.
            uploaded = await job_control.upload_file_creator5(
                Creator5UploadParams(
                    file_path=str(path),
                    start_print=False,
                    leveling_before_print=leveling_before_print,
                    use_matl_station=True,
                    gcode_tool_cnt=len(mappings),
                )
            )
            if not uploaded:
                raise JobStartError(f"The printer did not accept the upload of '{file_name}'.")
            started = await job_control.start_creator5_job(
                Creator5JobParams(
                    file_name=file_name,
                    leveling_before_print=leveling_before_print,
                    material_mappings=mappings,
                )
            )
            if not started:
                raise JobStartError(
                    f"'{file_name}' was uploaded, but the printer refused to start it. "
                    "Check the printer's screen."
                )
            return

        if plan == PLAN_AD5X_STATION:
            ok = await job_control.upload_file_ad5x(
                AD5XUploadParams(
                    file_path=str(path),
                    start_print=True,
                    leveling_before_print=leveling_before_print,
                    flow_calibration=False,
                    first_layer_inspection=False,
                    time_lapse_video=False,
                    material_mappings=mappings,
                )
            )
        else:
            ok = await job_control.upload_file(str(path), True, leveling_before_print)
    except JobStartError:
        raise
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        raise JobStartError(f"Error sending '{file_name}' to the printer: {err}") from err

    if not ok:
        raise JobStartError(
            f"The printer did not accept '{file_name}'. Check that it is idle and has "
            "room for the file."
        )


# --------------------------------------------------------------------------- #
# HTTP upload endpoint
# --------------------------------------------------------------------------- #


class FlashForgeUploadView(HomeAssistantView):
    """``POST /api/flashforge/upload`` - multipart ``entry_id`` then ``file``.

    Any logged-in user may upload, the same as starting a local print from the
    card. The file streams to disk; the request body is never read into memory.
    """

    url = "/api/flashforge/upload"
    name = "api:flashforge:upload"
    requires_auth = True

    def __init__(self, hass: HomeAssistant) -> None:
        self.hass = hass

    async def post(self, request: Any) -> Any:
        """Stage an upload and return the dialog payload."""
        try:
            reader = await request.multipart()
            part = await reader.next()
            if part is None or part.name != "entry_id":
                raise UploadError("The upload must start with the printer's entry_id.")
            entry_id = (await part.text()).strip()

            part = await reader.next()
            if part is None or part.name != "file":
                raise UploadError("No file was uploaded.")

            async def chunks() -> AsyncIterator[bytes]:
                while True:
                    chunk = await part.read_chunk(CHUNK_BYTES)
                    if not chunk:
                        return
                    yield chunk

            payload = await async_stage_upload(self.hass, entry_id, part.filename, chunks())
        except UploadError as err:
            return self.json_message(str(err), status_code=err.status)
        except Exception:  # noqa: BLE001 - a malformed request must not 500
            _LOGGER.exception("Unexpected error staging an upload")
            return self.json_message("The upload failed.", status_code=500)
        return self.json(payload)


# --------------------------------------------------------------------------- #
# Websocket commands
# --------------------------------------------------------------------------- #


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/upload/start",
        vol.Required("entry_id"): str,
        vol.Required("upload_id"): str,
        vol.Optional("leveling", default=False): bool,
        vol.Optional("material_mappings", default=list): vol.All(
            [MATERIAL_MAPPING_SCHEMA], vol.Length(max=MAX_SLOTS)
        ),
    }
)
@websocket_api.async_response
async def ws_upload_start(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Send a staged upload to the printer and start it."""
    data = hass.data.get(DOMAIN, {}).get(msg["entry_id"])
    if data is None:
        connection.send_error(
            msg["id"], ERR_ENTRY_NOT_FOUND, "That FlashForge printer is not set up."
        )
        return

    store = get_store(hass)
    staged = store.get(msg["upload_id"], msg["entry_id"])
    if staged is None:
        connection.send_error(
            msg["id"],
            ERR_UPLOAD_NOT_FOUND,
            "The uploaded file is no longer available. Select it again.",
        )
        return
    if staged.in_progress:
        connection.send_error(
            msg["id"], ERR_PRINTER, f"'{staged.file_name}' is already being sent."
        )
        return

    coordinator = data["coordinator"]
    machine_info = coordinator.data
    state = getattr(getattr(machine_info, "machine_state", None), "value", None)
    if state in BUSY_STATES:
        connection.send_error(
            msg["id"],
            ERR_PRINTER,
            f"The printer is {state}. Wait until it is idle, then start the upload.",
        )
        return

    slots = slots_to_list(machine_info)
    try:
        plan = upload_plan(machine_info, slots, staged.file_entry)
        mappings: list[AD5XMaterialMapping] = []
        if plan_requires_matching(plan):
            if not msg["material_mappings"]:
                raise HomeAssistantError(
                    f"'{staged.file_name}' needs its tools matched to Material Station "
                    "slots before it can start."
                )
            mappings = validate_mappings(staged.file_entry, slots, msg["material_mappings"])

        staged.in_progress = True
        try:
            await async_upload_and_print(
                data["client"],
                plan,
                staged.path,
                leveling_before_print=msg["leveling"],
                mappings=mappings,
            )
        finally:
            staged.in_progress = False
    except HomeAssistantError as err:
        connection.send_error(msg["id"], ERR_PRINTER, str(err))
        return
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        _LOGGER.exception("Unexpected error uploading %s", staged.file_name)
        connection.send_error(msg["id"], ERR_PRINTER, str(err))
        return

    await async_discard(hass, store, staged.upload_id)
    await coordinator.async_request_refresh()

    connection.send_result(
        msg["id"],
        {
            "started": True,
            "file_name": staged.file_name,
            "warnings": color_warnings(mappings),
        },
    )


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/upload/discard",
        vol.Required("entry_id"): str,
        vol.Required("upload_id"): str,
    }
)
@websocket_api.async_response
async def ws_upload_discard(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Delete a staged upload the user closed without starting."""
    store = get_store(hass)
    staged = store.get(msg["upload_id"], msg["entry_id"])
    if staged is not None and not staged.in_progress:
        await async_discard(hass, store, staged.upload_id)
    connection.send_result(msg["id"], {})
