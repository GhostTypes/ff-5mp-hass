"""Diagnostics support for the FlashForge integration."""
from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_CHECK_CODE,
    CONF_SERIAL_NUMBER,
    DOMAIN,
)
from .coordinator import FlashForgeDataUpdateCoordinator, FlashForgeFileListCoordinator

TO_REDACT_ENTRY = {CONF_CHECK_CODE, CONF_SERIAL_NUMBER}
TO_REDACT_DATA = {
    "flash_cloud_register_code",
    "polar_cloud_register_code",
    "mac_address",
    "ip_address",
}


def _machine_info_to_dict(data: Any) -> Any:
    """Convert an FFMachineInfo pydantic model to a JSON-serializable dict."""
    if data is None:
        return None
    if hasattr(data, "model_dump"):
        try:
            return data.model_dump(mode="json")
        except Exception:  # noqa: BLE001
            pass
    if hasattr(data, "dict"):
        try:
            return data.dict()
        except Exception:  # noqa: BLE001
            pass
    return repr(data)


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    file_coordinator: FlashForgeFileListCoordinator = hass.data[DOMAIN][entry.entry_id][
        "file_coordinator"
    ]
    client = hass.data[DOMAIN][entry.entry_id]["client"]

    machine_info = async_redact_data(
        _machine_info_to_dict(coordinator.data) or {}, TO_REDACT_DATA
    )

    return {
        "entry": {
            "title": entry.title,
            "data": async_redact_data(dict(entry.data), TO_REDACT_ENTRY),
            "options": dict(entry.options),
        },
        "coordinator": {
            "last_update_success": coordinator.last_update_success,
            "update_interval": (
                coordinator.update_interval.total_seconds()
                if coordinator.update_interval
                else None
            ),
            "device_model": coordinator.device_model,
        },
        "file_list": {
            "last_update_success": file_coordinator.last_update_success,
            "files": file_coordinator.file_names,
            "selected_file": file_coordinator.selected_file,
        },
        "capabilities": {
            "led_control": getattr(client, "led_control", None),
            "filtration_control": getattr(client, "filtration_control", None),
            "is_pro": getattr(client, "is_pro", None),
            "is_ad5x": getattr(client, "is_ad5x", None),
            "is_creator5": getattr(client, "is_creator5", None),
            "is_creator5_pro": getattr(client, "is_creator5_pro", None),
            "http_only": getattr(client, "http_only", None),
        },
        "machine_info": machine_info,
    }
