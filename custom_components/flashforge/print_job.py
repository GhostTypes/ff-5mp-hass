"""Starting prints of files that are already stored on the printer.

The printer exposes a single ``/printGcode`` endpoint, but the payload it expects
differs per model family. The library ships one method per family, so this module
holds the dispatch plus the Material Station mapping derivation shared by the
select entity, the button, and the ``flashforge.print_file`` service.
"""
from __future__ import annotations

import logging
import re
from typing import Any

from flashforge import FlashForgeClient
from flashforge.models import (
    AD5XLocalJobParams,
    AD5XMaterialMapping,
    AD5XSingleColorJobParams,
    Creator5JobParams,
    FFGcodeFileEntry,
    FFMachineInfo,
)

from homeassistant.exceptions import HomeAssistantError, ServiceValidationError

_LOGGER = logging.getLogger(__name__)

_HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")


def _is_hex_color(value: Any) -> bool:
    """Return True when the value is a ``#RRGGBB`` string the printer accepts."""
    return isinstance(value, str) and bool(_HEX_COLOR.match(value))


def _station_slot(machine_info: FFMachineInfo | None, slot_id: int) -> Any | None:
    """Return the Material Station slot info for a slot id, when reported."""
    station = getattr(machine_info, "matl_station_info", None)
    for slot in getattr(station, "slot_infos", None) or []:
        if getattr(slot, "slot_id", None) == slot_id:
            return slot
    return None


def needs_material_station(file_entry: FFGcodeFileEntry | None) -> bool:
    """Return True when the file was sliced for the Material Station.

    This can only be answered for printers whose ``/gcodeList`` carries the
    per-file detail (``gcodeListDetail``, e.g. the AD5X). The Creator 5 series
    returns plain file names, so ``use_matl_station`` and the tool data are
    unknown and this returns False - the file is then started without mappings
    and the printer falls back to the tool/slot assignment stored in the file.
    """
    return bool(
        file_entry is not None
        and getattr(file_entry, "use_matl_station", False)
        and getattr(file_entry, "gcode_tool_datas", None)
    )


def build_material_mappings(
    file_entry: FFGcodeFileEntry, machine_info: FFMachineInfo | None
) -> list[AD5XMaterialMapping]:
    """Derive the per-tool Material Station mappings for a file.

    The slot assignment comes from the file itself (the slicer stores a slot per
    tool); the slot color is taken from the printer's current Material Station
    report so the firmware sees the color of the filament actually loaded.

    Raises:
        ServiceValidationError: If the file's tool data is incomplete, in which
            case the mapping cannot be derived and the print must be started from
            the slicer or the FlashForge app.
    """
    mappings: list[AD5XMaterialMapping] = []

    for tool in file_entry.gcode_tool_datas or []:
        slot = _station_slot(machine_info, tool.slot_id)
        slot_color = getattr(slot, "material_color", "") or ""
        tool_color = tool.material_color or ""
        if not _is_hex_color(tool_color):
            tool_color = slot_color
        if not _is_hex_color(slot_color):
            slot_color = tool_color
        material = (tool.material_name or getattr(slot, "material_name", "") or "").strip()

        if (
            not 1 <= tool.slot_id <= 4
            or not material
            or not _is_hex_color(tool_color)
            or not _is_hex_color(slot_color)
        ):
            raise ServiceValidationError(
                f"Cannot derive the Material Station mapping for tool {tool.tool_id} of "
                f"'{file_entry.gcode_file_name}' (slot {tool.slot_id}, material "
                f"'{material or 'unknown'}'). Start this multi-material print from your "
                "slicer or the FlashForge app instead."
            )

        mappings.append(
            AD5XMaterialMapping(
                tool_id=tool.tool_id,
                slot_id=tool.slot_id,
                material_name=material,
                tool_material_color=tool_color,
                slot_material_color=slot_color,
            )
        )

    return mappings


async def async_start_local_print(
    client: FlashForgeClient,
    file_name: str,
    *,
    leveling_before_print: bool,
    file_entry: FFGcodeFileEntry | None = None,
    machine_info: FFMachineInfo | None = None,
) -> None:
    """Start a print of a file already stored on the printer.

    ``file_entry`` is the printer's file list entry for ``file_name``, when known;
    it is what tells us whether the file needs Material Station mappings. Without
    it - and on printers that report file names only, such as the Creator 5
    series - the file is started without mappings, leaving the printer to use the
    tool/slot assignment stored in the file itself.

    Raises:
        ServiceValidationError: If no file was given or the mappings cannot be
            derived from the file's tool data.
        HomeAssistantError: If the request fails or the printer rejects it.
    """
    file_name = (file_name or "").strip()
    if not file_name:
        raise ServiceValidationError("No file name given to print")

    mappings: list[AD5XMaterialMapping] = []
    if needs_material_station(file_entry):
        mappings = build_material_mappings(file_entry, machine_info)  # type: ignore[arg-type]

    _LOGGER.debug(
        "Starting print of %s (leveling=%s, material mappings=%d)",
        file_name,
        leveling_before_print,
        len(mappings),
    )

    try:
        if getattr(client, "is_creator5", False):
            started = await client.job_control.start_creator5_job(
                Creator5JobParams(
                    file_name=file_name,
                    leveling_before_print=leveling_before_print,
                    material_mappings=mappings or None,
                )
            )
        elif getattr(client, "is_ad5x", False):
            if mappings:
                started = await client.job_control.start_ad5x_multi_color_job(
                    AD5XLocalJobParams(
                        file_name=file_name,
                        leveling_before_print=leveling_before_print,
                        material_mappings=mappings,
                    )
                )
            else:
                started = await client.job_control.start_ad5x_single_color_job(
                    AD5XSingleColorJobParams(
                        file_name=file_name,
                        leveling_before_print=leveling_before_print,
                    )
                )
        else:
            started = await client.job_control.print_local_file(
                file_name, leveling_before_print
            )
    except HomeAssistantError:
        raise
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        raise HomeAssistantError(f"Error starting print of '{file_name}': {err}") from err

    if not started:
        raise HomeAssistantError(
            f"The printer rejected the request to print '{file_name}'. Make sure the "
            "file is still on the printer and the printer is idle."
        )
