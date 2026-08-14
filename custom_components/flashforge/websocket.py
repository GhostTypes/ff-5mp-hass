"""WebSocket API backing the FlashForge job card.

The card is a plain custom element with no state of its own; everything it shows
comes from these four commands, and every action it takes goes back through them.
Commands rather than entities because a file list is a *request*, not a state: it
is only interesting while the card is open, it carries per-file metadata far too
large for entity attributes, and thumbnails are not expressible as state at all.

    flashforge/files/list      list the files on the printer, plus the slots
    flashforge/file/thumbnail  one file's thumbnail, base64 PNG
    flashforge/job/prepare     what starting this file would involve
    flashforge/job/start       start it

Note that `job/prepare` is advisory: it returns a *suggested* mapping for the
card to pre-fill so the common case is one click, but `job/start` re-validates
whatever comes back against the live printer state. Nothing the card sends is
taken on trust.
"""
from __future__ import annotations

import base64
import logging
from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator
from .job import (
    async_start_local_print,
    auto_match,
    color_warnings,
    file_to_dict,
    requires_material_matching,
    slots_to_list,
    validate_mappings,
)
from .util import is_creator5_series

_LOGGER = logging.getLogger(__name__)

_REGISTERED_KEY = f"{DOMAIN}_websocket_registered"

ERR_ENTRY_NOT_FOUND = "entry_not_found"
ERR_FILE_NOT_FOUND = "file_not_found"
ERR_PRINTER = "printer_error"

# Thumbnails are fetched per file and never change for a given name, so they are
# worth keeping - but a printer can hold many files and the payloads are images.
# Cap the cache and evict oldest-first; the cost of a miss is one HTTP request.
_THUMBNAIL_CACHE_SIZE = 24

MATERIAL_MAPPING_SCHEMA = vol.Schema(
    {
        vol.Required("tool_id"): int,
        vol.Required("slot_id"): int,
    },
    # The card also echoes back material_name and the colors. They are ignored:
    # job.validate_mappings re-derives all of them from the file and the live
    # station report, so a stale card cannot misdescribe what is loaded.
    extra=vol.ALLOW_EXTRA,
)


@callback
def async_register_websocket_commands(hass: HomeAssistant) -> None:
    """Register the job-card websocket commands, once per Home Assistant run."""
    if hass.data.get(_REGISTERED_KEY):
        return
    hass.data[_REGISTERED_KEY] = True

    websocket_api.async_register_command(hass, ws_list_entries)
    websocket_api.async_register_command(hass, ws_list_files)
    websocket_api.async_register_command(hass, ws_file_thumbnail)
    websocket_api.async_register_command(hass, ws_prepare_job)
    websocket_api.async_register_command(hass, ws_start_job)


def _entry_data(hass: HomeAssistant, entry_id: str) -> dict[str, Any] | None:
    """Return the stored runtime data for a config entry, if it is loaded."""
    return hass.data.get(DOMAIN, {}).get(entry_id)


async def _async_fetch_files(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Fetch and normalize the printer's file list.

    Every supported model answers ``/gcodeList`` with its ten most recent files;
    the full local listing exists only over the legacy TCP channel this
    integration deliberately does not speak. The AD5X and Creator 5 series
    include per-tool material data here, which is what makes matching possible.
    """
    client = data["client"]
    entries = await client.files.get_recent_file_list()
    return [file_to_dict(entry) for entry in entries or []]


@websocket_api.websocket_command({vol.Required("type"): "flashforge/entries"})
@callback
def ws_list_entries(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """List the set-up FlashForge printers, for the card's config editor."""
    entries = [
        {"entry_id": entry_id, "title": data["name"]}
        for entry_id, data in hass.data.get(DOMAIN, {}).items()
        if isinstance(data, dict) and "name" in data
    ]
    connection.send_result(msg["id"], {"entries": entries})


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/files/list",
        vol.Required("entry_id"): str,
    }
)
@websocket_api.async_response
async def ws_list_files(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return the printer's files plus the current Material Station state."""
    data = _entry_data(hass, msg["entry_id"])
    if data is None:
        connection.send_error(
            msg["id"], ERR_ENTRY_NOT_FOUND, "That FlashForge printer is not set up."
        )
        return

    coordinator: FlashForgeDataUpdateCoordinator = data["coordinator"]

    try:
        files = await _async_fetch_files(data)
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        _LOGGER.warning("Could not list files on %s: %s", data["name"], err)
        connection.send_error(
            msg["id"], ERR_PRINTER, f"Could not read the printer's file list: {err}"
        )
        return

    slots = slots_to_list(coordinator.data)
    machine_state = getattr(coordinator.data, "machine_state", None)

    connection.send_result(
        msg["id"],
        {
            "printer_name": data["name"],
            "model": coordinator.device_model,
            "files": files,
            "slots": slots,
            "has_material_station": bool(slots),
            # The Creator 5 series cannot start a previously-uploaded local job
            # over the HTTP API (only a fresh 3mf upload+start works), so the
            # card shows an info message in place of the file list / Start button.
            "is_creator5_series": is_creator5_series(coordinator.data),
            # Advisory only - the printer is the one that refuses a print while
            # it is busy, and it is better at knowing than we are.
            "machine_state": getattr(machine_state, "value", None),
        },
    )


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/file/thumbnail",
        vol.Required("entry_id"): str,
        vol.Required("file_name"): str,
    }
)
@websocket_api.async_response
async def ws_file_thumbnail(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return one file's thumbnail as a base64 PNG, or null if it has none."""
    data = _entry_data(hass, msg["entry_id"])
    if data is None:
        connection.send_error(
            msg["id"], ERR_ENTRY_NOT_FOUND, "That FlashForge printer is not set up."
        )
        return

    file_name: str = msg["file_name"]
    cache: dict[str, str | None] = data.setdefault("thumbnail_cache", {})

    if file_name in cache:
        connection.send_result(msg["id"], {"image": cache[file_name]})
        return

    try:
        raw = await data["client"].files.get_gcode_thumbnail(file_name)
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        # A missing thumbnail is not a failure worth showing the user; the card
        # falls back to a placeholder tile.
        _LOGGER.debug("No thumbnail for %s: %s", file_name, err)
        raw = None

    image = base64.b64encode(raw).decode("ascii") if raw else None

    if len(cache) >= _THUMBNAIL_CACHE_SIZE:
        cache.pop(next(iter(cache)))
    cache[file_name] = image

    connection.send_result(msg["id"], {"image": image})


def _find_file(
    files: list[dict[str, Any]], file_name: str
) -> dict[str, Any] | None:
    """Return the listed file with this name, if the printer still reports it."""
    return next((item for item in files if item["file_name"] == file_name), None)


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/job/prepare",
        vol.Required("entry_id"): str,
        vol.Required("file_name"): str,
    }
)
@websocket_api.async_response
async def ws_prepare_job(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Describe what starting this file involves, and suggest a mapping.

    The card opens the matching dialog on the strength of this answer: it says
    whether the file needs matching at all, what the tools and slots are, and
    which slot each tool would sensibly come from. The suggestion is pre-filled
    for the user to confirm or change - it is never started on its own.
    """
    data = _entry_data(hass, msg["entry_id"])
    if data is None:
        connection.send_error(
            msg["id"], ERR_ENTRY_NOT_FOUND, "That FlashForge printer is not set up."
        )
        return

    coordinator: FlashForgeDataUpdateCoordinator = data["coordinator"]

    try:
        files = await _async_fetch_files(data)
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        connection.send_error(
            msg["id"], ERR_PRINTER, f"Could not read the printer's file list: {err}"
        )
        return

    file_entry = _find_file(files, msg["file_name"])
    if file_entry is None:
        connection.send_error(
            msg["id"],
            ERR_FILE_NOT_FOUND,
            f"'{msg['file_name']}' is no longer on the printer.",
        )
        return

    slots = slots_to_list(coordinator.data)
    needs_matching = requires_material_matching(file_entry, slots)
    suggested = auto_match(file_entry, slots) if needs_matching else []

    connection.send_result(
        msg["id"],
        {
            "file": file_entry,
            "slots": slots,
            "requires_matching": needs_matching,
            "suggested_mappings": suggested,
            # True when every tool got a suggestion, i.e. the user only has to
            # confirm. False means at least one tool is still theirs to map.
            "suggestion_complete": needs_matching
            and len(suggested) == len(file_entry["tool_datas"]),
        },
    )


@websocket_api.websocket_command(
    {
        vol.Required("type"): "flashforge/job/start",
        vol.Required("entry_id"): str,
        vol.Required("file_name"): str,
        vol.Optional("leveling", default=False): bool,
        vol.Optional("material_mappings", default=list): vol.All(
            [MATERIAL_MAPPING_SCHEMA], vol.Length(max=4)
        ),
    }
)
@websocket_api.async_response
async def ws_start_job(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Start a print of a file already on the printer."""
    data = _entry_data(hass, msg["entry_id"])
    if data is None:
        connection.send_error(
            msg["id"], ERR_ENTRY_NOT_FOUND, "That FlashForge printer is not set up."
        )
        return

    coordinator: FlashForgeDataUpdateCoordinator = data["coordinator"]
    file_name: str = msg["file_name"]
    requested = msg["material_mappings"]

    try:
        files = await _async_fetch_files(data)
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        connection.send_error(
            msg["id"], ERR_PRINTER, f"Could not read the printer's file list: {err}"
        )
        return

    file_entry = _find_file(files, file_name)
    if file_entry is None:
        connection.send_error(
            msg["id"],
            ERR_FILE_NOT_FOUND,
            f"'{file_name}' is no longer on the printer.",
        )
        return

    slots = slots_to_list(coordinator.data)

    try:
        mappings = (
            validate_mappings(file_entry, slots, requested) if requested else []
        )

        if not mappings and requires_material_matching(file_entry, slots):
            # Reached only by a client that skipped the dialog. Starting anyway
            # would let the printer fall back to the slot assignment baked into
            # the file, which may point at filament that is no longer loaded.
            raise HomeAssistantError(
                f"'{file_name}' needs its tools matched to Material Station slots "
                "before it can start."
            )

        await async_start_local_print(
            data["client"],
            file_name,
            leveling_before_print=msg["leveling"],
            mappings=mappings,
        )
    except HomeAssistantError as err:
        connection.send_error(msg["id"], ERR_PRINTER, str(err))
        return
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        _LOGGER.exception("Unexpected error starting %s", file_name)
        connection.send_error(msg["id"], ERR_PRINTER, str(err))
        return

    await coordinator.async_request_refresh()

    connection.send_result(
        msg["id"],
        {
            "started": True,
            "file_name": file_name,
            "warnings": color_warnings(mappings),
        },
    )
