"""Utility helpers for the FlashForge integration."""
from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, MANUFACTURER

if TYPE_CHECKING:
    from flashforge import FlashForgeClient
    from flashforge.models import FFMachineInfo

    from .coordinator import FlashForgeDataUpdateCoordinator


async def async_close_flashforge_client(client: "FlashForgeClient") -> None:
    """Close any HTTP resources held by the FlashForge client without touching TCP."""
    session = getattr(client, "_http_session", None)
    if session and not session.closed:
        await session.close()


def build_device_info(
    coordinator: "FlashForgeDataUpdateCoordinator",
    printer_name: str,
    entry_id: str,
) -> DeviceInfo:
    """Return the shared DeviceInfo for FlashForge entities."""
    return DeviceInfo(
        identifiers={(DOMAIN, entry_id)},
        name=printer_name,
        manufacturer=MANUFACTURER,
        model=coordinator.device_model,
    )


def is_creator5_series(data: FFMachineInfo) -> bool:
    """Creator 5 / Creator 5 Pro (the 4-tool tool-changer family).

    Identity is derived from the firmware-set ``pid`` on ``/detail`` (exposed by
    the library as ``is_creator5`` / ``is_creator5_pro``), never from the
    user-mutable printer ``name`` - see CLAUDE.md / AGENTS.md. Used to gate both
    entities (sensor toolhead availability) and the job card's local-print flow,
    which the Creator 5 series cannot service over the local HTTP API.
    """
    return bool(
        getattr(data, "is_creator5", False) or getattr(data, "is_creator5_pro", False)
    )
