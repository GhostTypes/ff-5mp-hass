"""Utility helpers for the FlashForge integration."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, MANUFACTURER

if TYPE_CHECKING:
    from flashforge import FlashForgeClient

    from .coordinator import FlashForgeDataUpdateCoordinator


def has_material_station(data: Any) -> bool:
    """Return True when the printer has a Material Station attached.

    ``FFMachineInfo.has_matl_station`` mirrors the raw ``hasMatlStation`` field
    from ``/detail``, which the Creator 5 series does not report at all — it
    arrives as ``None`` even when ``matlStationInfo`` is fully populated with
    four loaded slots. Treat populated slot data as proof of the station, the
    same way the library's own AD5X heuristic does, so the flag being absent
    does not hide the entities on a Creator 5 / Creator 5 Pro.
    """
    if data is None:
        return False
    if getattr(data, "has_matl_station", None) is True:
        return True
    station = getattr(data, "matl_station_info", None)
    if station is None:
        return False
    if (getattr(station, "slot_cnt", 0) or 0) > 0:
        return True
    return bool(getattr(station, "slot_infos", None))


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
