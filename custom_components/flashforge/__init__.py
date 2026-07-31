"""The FlashForge 3D Printer integration."""
from __future__ import annotations

import logging

from flashforge import (
    FiveMClientConnectionOptions,
    FlashForgeClient,
    FlashForgeResponseError,
)

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.loader import async_get_integration

from .const import (
    CONF_CHECK_CODE,
    CONF_SCAN_INTERVAL,
    CONF_SERIAL_NUMBER,
    CONF_OVERRIDE_LED_AVAILABILITY,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
)
from .coordinator import FlashForgeDataUpdateCoordinator
from .card import async_register_frontend
from .util import async_close_flashforge_client
from .websocket import async_register_websocket_commands

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.SWITCH,
    Platform.SELECT,
    Platform.BUTTON,
    Platform.CAMERA,
    Platform.IMAGE,
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up FlashForge from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Register the job card and its websocket commands FIRST, before anything
    # that talks to the printer. Both are global, printer-independent, and
    # cheap - and everything below this point can raise ConfigEntryNotReady.
    # Registering afterwards meant an offline printer took the card down with
    # it: the module URL was never added to the frontend, so the card did not
    # exist in the picker and dashboards using it showed "custom element
    # doesn't exist" until the printer came back.
    async_register_websocket_commands(hass)
    integration = await async_get_integration(hass, DOMAIN)
    await async_register_frontend(hass, str(integration.version))

    # Extract configuration
    ip_address = entry.data[CONF_IP_ADDRESS]
    serial_number = entry.data[CONF_SERIAL_NUMBER]
    check_code = entry.data[CONF_CHECK_CODE]
    name = entry.data.get(CONF_NAME, "FlashForge Printer")
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
    override_led_availability = entry.options.get(CONF_OVERRIDE_LED_AVAILABILITY, False)

    # Create FlashForge client.
    #
    # `led_control_override` is tri-state, not a boolean: None means "no
    # override, trust /product", True forces the capability on, and False forces
    # it OFF. Passing the option straight through sent False whenever the user
    # had not enabled it - the default - which vetoed the printer's own correct
    # capability report and greyed out the LED switch on every model. Only ever
    # force the capability when the user actually asked for it.
    client = FlashForgeClient(
        ip_address=ip_address,
        serial_number=serial_number,
        check_code=check_code,
        options=FiveMClientConnectionOptions(
            led_control_override=True if override_led_availability else None,
        ),
    )

    # Initialize the client via HTTP only
    try:
        machine_info = await client.info.get()
    except FlashForgeResponseError as err:
        # Still ConfigEntryNotReady - a firmware payload we cannot read may well
        # become readable after an integration update, so HA should keep
        # retrying. The distinction is in the message, which has to send the
        # user to the issue tracker rather than to their router (issue #18).
        _LOGGER.error(
            "The printer answered, but its response could not be read. This is an "
            "integration bug, not a connection problem - please report it at "
            "https://github.com/GhostTypes/ff-5mp-hass/issues with debug logs enabled. %s",
            err,
        )
        await async_close_flashforge_client(client)
        raise ConfigEntryNotReady(
            f"The printer's response could not be read (this is not a connectivity "
            f"problem; please report it): {err}"
        ) from err
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
            # Not necessarily a credential problem: the library returns False
            # both when the printer refuses and when the response could not be
            # parsed. It logs the two distinctly (flashforge-python-api >=
            # 1.3.3), so point there rather than asserting the check code is
            # wrong - that assertion is what made issue #18 unreadable.
            raise ConfigEntryNotReady(
                "The printer did not accept the /product request. This usually means the "
                "serial number or check code is wrong, but an unreadable response looks "
                "the same from here - check the log for the specific cause."
            )
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
