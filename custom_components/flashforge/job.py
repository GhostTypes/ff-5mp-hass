"""Local print jobs: file listing, material matching, and job start.

This is the Home Assistant port of the FlashForgeUI job picker plus its material
matching dialog. Three things live here, in the order the card uses them:

1. **Normalization** - turn the library's ``FFGcodeFileEntry`` and
   ``MatlStationInfo`` into the flat, JSON-safe dicts the card renders.
2. **Matching rules** - the validation FlashForgeUI applies before it will let a
   job start, reimplemented server-side. The card enforces the same rules while
   the user clicks, but the card is untrusted: a websocket client can send any
   mapping it likes, so :func:`validate_mappings` is what actually decides.
3. **Dispatch** - the per-model print-start command. Every model reaches the same
   ``/printGcode`` endpoint but expects a different payload, so the library ships
   one method per family and this module picks between them.

The matching rules, verbatim from the desktop app:

* every tool in the file must be mapped, exactly once;
* a slot may back at most one tool;
* an empty slot cannot be used;
* the material names must match (case- and whitespace-insensitively) - a
  mismatch is an error, not a warning;
* a *color* difference is allowed and only produces a warning. The print will
  come out the wrong color, which is the user's business, not ours.
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

from homeassistant.exceptions import HomeAssistantError

_LOGGER = logging.getLogger(__name__)

_HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")

# Sent to the printer when a slot or tool reports no usable color. The firmware
# validates the shape of these fields but does nothing with the value for a
# single-color job, and a neutral grey is what the desktop app sends.
FALLBACK_COLOR = "#808080"

MAX_SLOTS = 4


class MaterialMatchingError(HomeAssistantError):
    """The requested tool-to-slot mapping is not one the printer should be sent."""


class JobStartError(HomeAssistantError):
    """The printer refused the print, or could not be asked."""


# --------------------------------------------------------------------------- #
# Normalization
# --------------------------------------------------------------------------- #


def normalize_material(value: str | None) -> str:
    """Fold a material name for comparison (FlashForgeUI's normalizeMaterialString)."""
    return (value or "").strip().lower()


def is_hex_color(value: Any) -> bool:
    """Return True for a ``#RRGGBB`` string, the only color form the printer takes."""
    return isinstance(value, str) and bool(_HEX_COLOR.match(value))


def _color_or_fallback(value: str | None) -> str:
    """Return a printer-acceptable color, substituting grey for anything else."""
    return value if is_hex_color(value) else FALLBACK_COLOR


def tool_to_dict(tool: Any) -> dict[str, Any]:
    """Describe one tool requirement of a file for the card."""
    return {
        "tool_id": getattr(tool, "tool_id", 0),
        "material_name": getattr(tool, "material_name", "") or "",
        "material_color": getattr(tool, "material_color", "") or "",
        "filament_weight": getattr(tool, "filament_weight", 0.0) or 0.0,
        # The slot the *slicer* assigned. Only a hint for pre-filling; the
        # printer is told whatever the user confirms.
        "slot_id": getattr(tool, "slot_id", 0),
    }


def file_to_dict(entry: FFGcodeFileEntry) -> dict[str, Any]:
    """Describe one file for the card.

    Fields the printer did not report stay ``None`` rather than becoming 0 or
    False: on the Creator 5 series ``/gcodeList`` returns bare file names, and a
    multi-material file there must not be rendered as a confirmed single-material
    one.
    """
    tools = [tool_to_dict(tool) for tool in entry.gcode_tool_datas or []]
    return {
        "file_name": entry.gcode_file_name,
        "printing_time": entry.printing_time or None,
        "total_filament_weight": entry.total_filament_weight,
        "tool_count": entry.gcode_tool_cnt,
        "use_matl_station": entry.use_matl_station,
        "tool_datas": tools,
    }


def slots_to_list(machine_info: FFMachineInfo | None) -> list[dict[str, Any]]:
    """Describe the Material Station slots for the card.

    Returns an empty list when the printer has no station or has not reported it
    yet; the card treats that as "no material matching possible".
    """
    station = getattr(machine_info, "matl_station_info", None)
    slots: list[dict[str, Any]] = []
    for slot in getattr(station, "slot_infos", None) or []:
        slot_id = getattr(slot, "slot_id", 0)
        if not 1 <= slot_id <= MAX_SLOTS:
            # A station reporting a fifth slot is a slot we ignore, not an error
            # (the printer cannot be told about it - slotId is validated 1-4).
            continue
        has_filament = bool(getattr(slot, "has_filament", False))
        material = getattr(slot, "material_name", "") or ""
        slots.append(
            {
                "slot_id": slot_id,
                "is_empty": not has_filament or not material,
                "material_name": material,
                "material_color": getattr(slot, "material_color", "") or "",
            }
        )
    slots.sort(key=lambda item: item["slot_id"])
    return slots


def requires_material_matching(
    file_entry: dict[str, Any], slots: list[dict[str, Any]]
) -> bool:
    """Return True when this file needs the user to map tools to slots.

    Requires both sides of the mapping to be knowable: the file's per-tool data
    and a reporting Material Station. A file with a single tool still goes
    through matching when the printer has a station - the desktop app does the
    same, because the one tool still has to be told which slot to pull from.
    """
    return bool(slots) and bool(file_entry.get("tool_datas"))


# --------------------------------------------------------------------------- #
# Matching
# --------------------------------------------------------------------------- #


def auto_match(
    file_entry: dict[str, Any], slots: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Suggest a tool-to-slot mapping for the card to pre-fill.

    Best effort and deliberately incomplete when it cannot be sure: any tool it
    cannot place is simply left out, and the user maps it by hand. The result is
    a suggestion shown for confirmation, never something acted on directly -
    :func:`validate_mappings` still has the final say when the user confirms.

    Preference order per tool, over slots not already taken:

    1. the slicer's own slot assignment, if that slot's material matches;
    2. a material *and* color match;
    3. a material match.
    """
    available = {
        slot["slot_id"]: slot for slot in slots if not slot["is_empty"]
    }
    taken: set[int] = set()
    matches: list[dict[str, Any]] = []

    for tool in file_entry.get("tool_datas") or []:
        wanted = normalize_material(tool["material_name"])
        if not wanted:
            continue

        candidates = [
            slot
            for slot_id, slot in available.items()
            if slot_id not in taken
            and normalize_material(slot["material_name"]) == wanted
        ]
        if not candidates:
            continue

        hinted = tool.get("slot_id") or 0
        chosen = next((s for s in candidates if s["slot_id"] == hinted), None)
        if chosen is None:
            tool_color = normalize_material(tool["material_color"])
            chosen = next(
                (
                    s
                    for s in candidates
                    if tool_color
                    and normalize_material(s["material_color"]) == tool_color
                ),
                None,
            )
        if chosen is None:
            chosen = candidates[0]

        taken.add(chosen["slot_id"])
        matches.append(build_mapping(tool, chosen))

    return matches


def build_mapping(tool: dict[str, Any], slot: dict[str, Any]) -> dict[str, Any]:
    """Build one mapping entry from a tool requirement and the slot backing it."""
    return {
        "tool_id": tool["tool_id"],
        "slot_id": slot["slot_id"],
        "material_name": (tool["material_name"] or slot["material_name"]).strip(),
        "tool_material_color": _color_or_fallback(tool["material_color"]),
        "slot_material_color": _color_or_fallback(slot["material_color"]),
    }


def validate_mappings(
    file_entry: dict[str, Any],
    slots: list[dict[str, Any]],
    mappings: list[dict[str, Any]],
) -> list[AD5XMaterialMapping]:
    """Check a mapping set against the printer's state and return it for sending.

    This is the authority, not the card: it re-derives every material name and
    color from the file and the live station report rather than trusting what the
    client sent, so a stale card cannot tell the printer that an empty slot holds
    PLA.

    Raises:
        MaterialMatchingError: If the mapping is incomplete, double-books a slot,
            uses an empty or unknown slot, or pairs mismatched materials.
    """
    tools = {tool["tool_id"]: tool for tool in file_entry.get("tool_datas") or []}
    slots_by_id = {slot["slot_id"]: slot for slot in slots}

    if len(mappings) != len(tools):
        raise MaterialMatchingError(
            f"This file needs {len(tools)} tool(s) mapped to slots, "
            f"but {len(mappings)} mapping(s) were given."
        )

    seen_tools: set[int] = set()
    seen_slots: set[int] = set()
    resolved: list[AD5XMaterialMapping] = []

    for mapping in mappings:
        tool_id = mapping.get("tool_id")
        slot_id = mapping.get("slot_id")

        tool = tools.get(tool_id)
        if tool is None:
            raise MaterialMatchingError(
                f"Tool {tool_id} is not used by this file."
            )
        if tool_id in seen_tools:
            raise MaterialMatchingError(
                f"Tool {tool_id + 1} was mapped more than once."
            )
        seen_tools.add(tool_id)

        slot = slots_by_id.get(slot_id)
        if slot is None:
            raise MaterialMatchingError(
                f"Slot {slot_id} is not reported by the Material Station."
            )
        if slot_id in seen_slots:
            raise MaterialMatchingError(
                f"Slot {slot_id} is already assigned to another tool."
            )
        seen_slots.add(slot_id)

        if slot["is_empty"]:
            raise MaterialMatchingError(
                f"Slot {slot_id} is empty. Load filament before starting this print."
            )

        if normalize_material(tool["material_name"]) != normalize_material(
            slot["material_name"]
        ):
            raise MaterialMatchingError(
                f"Material mismatch: tool {tool_id + 1} requires "
                f"{tool['material_name'] or 'an unknown material'}, but slot "
                f"{slot_id} contains {slot['material_name'] or 'no material'}."
            )

        built = build_mapping(tool, slot)
        resolved.append(
            AD5XMaterialMapping(
                tool_id=built["tool_id"],
                slot_id=built["slot_id"],
                material_name=built["material_name"],
                tool_material_color=built["tool_material_color"],
                slot_material_color=built["slot_material_color"],
            )
        )

    return resolved


def color_warnings(mappings: list[AD5XMaterialMapping]) -> list[str]:
    """Describe the mappings whose tool and slot colors differ.

    Never blocking - the desktop app allows a color difference and only says so,
    because it prints fine, just not in the color the file was sliced for.
    """
    return [
        f"Tool {mapping.tool_id + 1} expects {mapping.tool_material_color} but slot "
        f"{mapping.slot_id} holds {mapping.slot_material_color}. The print will "
        f"start, but its colors will differ."
        for mapping in mappings
        if normalize_material(mapping.tool_material_color)
        != normalize_material(mapping.slot_material_color)
    ]


# --------------------------------------------------------------------------- #
# Dispatch
# --------------------------------------------------------------------------- #


async def async_start_local_print(
    client: FlashForgeClient,
    file_name: str,
    *,
    leveling_before_print: bool,
    mappings: list[AD5XMaterialMapping] | None = None,
) -> None:
    """Start a print of a file already stored on the printer.

    Every model posts to ``/printGcode``, but each family expects a different
    payload, so the library exposes one method per family:

    * **Creator 5 / 5 Pro** - one call, mappings included. The C5 registers the
      tool count at *upload* time, so the print-start carries only the mappings
      (or none, for a single-tool file).
    * **AD5X** - two commands, chosen by whether mappings are present: the
      multi-color one sets ``useMatlStation``, the single-color one clears it.
    * **5M / 5M Pro** - no material station; the plain local-print command.

    Raises:
        JobStartError: If the request fails or the printer rejects the print.
    """
    mappings = mappings or []

    _LOGGER.debug(
        "Starting print of %s (leveling=%s, mappings=%d)",
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
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        raise JobStartError(f"Error starting print of '{file_name}': {err}") from err

    if not started:
        raise JobStartError(
            f"The printer rejected the request to print '{file_name}'. Check that the "
            "file is still on the printer and that the printer is idle."
        )
