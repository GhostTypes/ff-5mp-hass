"""Utility helpers for the FlashForge integration."""
from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, MANUFACTURER

if TYPE_CHECKING:
    from flashforge import FlashForgeClient

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
