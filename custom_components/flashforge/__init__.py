"""The FlashForge 3D Printer integration."""
from __future__ import annotations

import logging

from flashforge import FlashForgeClient

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
    CONF_CHECK_CODE,
    CONF_SCAN_INTERVAL,
    CONF_SERIAL_NUMBER,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
)
from .coordinator import FlashForgeDataUpdateCoordinator
from .util import async_close_flashforge_client

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.BUTTON,
    Platform.CAMERA,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up FlashForge from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Extract configuration
    ip_address = entry.data[CONF_IP_ADDRESS]
    serial_number = entry.data[CONF_SERIAL_NUMBER]
    check_code = entry.data[CONF_CHECK_CODE]
    name = entry.data.get(CONF_NAME, "FlashForge Printer")
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)

    # Create FlashForge client
    client = FlashForgeClient(
        ip_address=ip_address,
        serial_number=serial_number,
        check_code=check_code,
    )

    # Initialize the client via HTTP only
    try:
        machine_info = await client.info.get()
    except Exception as err:  # noqa: BLE001 - upstream may raise broad exceptions
        _LOGGER.error("Error retrieving printer status: %s", err)
        await async_close_flashforge_client(client)
        raise ConfigEntryNotReady(f"Error retrieving printer status: {err}") from err

    if machine_info is None:
        await async_close_flashforge_client(client)
        raise ConfigEntryNotReady(f"Failed to retrieve printer information from {ip_address}")

    client.cache_details(machine_info)

    try:
        if not await client.send_product_command():
            await async_close_flashforge_client(client)
            raise ConfigEntryNotReady("Printer rejected credentials; check code may be invalid")
    except Exception as err:  # noqa: BLE001
        _LOGGER.error("Error validating printer credentials: %s", err)
        await async_close_flashforge_client(client)
        raise ConfigEntryNotReady(f"Error validating printer credentials: {err}") from err

    # Create coordinator
    coordinator = FlashForgeDataUpdateCoordinator(
        hass=hass,
        client=client,
        name=name,
        scan_interval=scan_interval,
    )

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator and client
    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
        "client": client,
        "name": name,
    }

    # Set up platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register update listener for options changes
    entry.async_on_unload(entry.add_update_listener(async_update_options))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        # Clean up coordinator and client
        data = hass.data[DOMAIN].pop(entry.entry_id)
        coordinator: FlashForgeDataUpdateCoordinator = data["coordinator"]
        await coordinator.async_shutdown()

    return unload_ok


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update options."""
    await hass.config_entries.async_reload(entry.entry_id)
