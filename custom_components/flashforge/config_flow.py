"""Config flow for FlashForge integration."""
from __future__ import annotations

import logging
from typing import Any

from flashforge import FlashForgeClient, FlashForgePrinterDiscovery
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME
from homeassistant.core import HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_CHECK_CODE,
    CONF_SCAN_INTERVAL,
    CONF_SERIAL_NUMBER,
    DEFAULT_NAME,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
)
from .util import async_close_flashforge_client

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("discovery_mode", default="auto"): vol.In(
            {"auto": "Automatic Discovery", "manual": "Manual Entry"}
        ),
    }
)

STEP_DISCOVERY_SCHEMA = vol.Schema({})

STEP_MANUAL_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_IP_ADDRESS): cv.string,
        vol.Required(CONF_SERIAL_NUMBER): cv.string,
        vol.Required(CONF_CHECK_CODE): cv.string,
    }
)


async def validate_connection(
    hass: HomeAssistant, data: dict[str, Any]
) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    client = FlashForgeClient(
        ip_address=data[CONF_IP_ADDRESS],
        serial_number=data[CONF_SERIAL_NUMBER],
        check_code=data[CONF_CHECK_CODE],
    )

    try:
        # Query printer status via HTTP API
        machine_info = await client.info.get()
        if machine_info is None:
            raise ConnectionError("Failed to retrieve printer information")

        # Validate credentials using the product endpoint (HTTP only)
        if not await client.send_product_command():
            raise ConnectionError("Printer rejected the provided credentials")

        # Cache details for consistency with the core client
        client.cache_details(machine_info)

        return {
            "title": data.get(CONF_NAME, DEFAULT_NAME),
            "machine_name": machine_info.name or DEFAULT_NAME,
        }

    finally:
        await async_close_flashforge_client(client)


class FlashForgeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for FlashForge."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self.discovered_printers: list[dict[str, Any]] = []
        self.discovery_mode: str = "auto"
        self._printer_data: dict[str, Any] = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step - choose discovery mode."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=STEP_USER_DATA_SCHEMA,
            )

        self.discovery_mode = user_input["discovery_mode"]

        if self.discovery_mode == "auto":
            return await self.async_step_discovery()
        else:
            return await self.async_step_manual()

    async def async_step_discovery(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle automatic discovery of printers."""
        errors: dict[str, str] = {}

        if user_input is None:
            # Perform discovery
            try:
                discovery = FlashForgePrinterDiscovery()
                printers = await discovery.discover_printers_async(timeout_ms=5000)

                if not printers:
                    errors["base"] = "no_printers_found"
                else:
                    self.discovered_printers = [
                        {
                            CONF_NAME: printer.name,
                            CONF_IP_ADDRESS: printer.ip_address,
                            CONF_SERIAL_NUMBER: printer.serial_number,
                        }
                        for printer in printers
                    ]

                    # If only one printer found, auto-select it
                    if len(self.discovered_printers) == 1:
                        self._printer_data = self.discovered_printers[0]
                        return await self.async_step_credentials()

                    # Multiple printers found - let user choose
                    return await self.async_step_select_printer()

            except Exception as err:
                _LOGGER.error("Error during printer discovery: %s", err)
                errors["base"] = "discovery_failed"

        if errors:
            return self.async_show_form(
                step_id="discovery",
                data_schema=STEP_DISCOVERY_SCHEMA,
                errors=errors,
                description_placeholders={
                    "error": "Could not discover printers. Try manual entry instead."
                },
            )

        return self.async_show_form(
            step_id="discovery",
            data_schema=STEP_DISCOVERY_SCHEMA,
        )

    async def async_step_select_printer(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle selection from multiple discovered printers."""
        if user_input is not None:
            selected_name = user_input["printer"]
            selected_printer = next(
                (p for p in self.discovered_printers if p[CONF_NAME] == selected_name),
                None,
            )
            if selected_printer:
                # Store printer data for credentials step
                self._printer_data = selected_printer
                return await self.async_step_credentials()

        # Create list of printer names for selection
        printer_names = {p[CONF_NAME]: p[CONF_NAME] for p in self.discovered_printers}

        return self.async_show_form(
            step_id="select_printer",
            data_schema=vol.Schema(
                {
                    vol.Required("printer"): vol.In(printer_names),
                }
            ),
        )

    async def async_step_credentials(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle credentials entry for discovered printer."""
        errors: dict[str, str] = {}

        # If user submitted the check code form
        if user_input is not None:
            # Merge check code with stored printer data
            printer_data = {**self._printer_data, CONF_CHECK_CODE: user_input[CONF_CHECK_CODE]}

            try:
                info = await validate_connection(self.hass, printer_data)

                # Check if already configured
                await self.async_set_unique_id(printer_data[CONF_SERIAL_NUMBER])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=info["title"],
                    data={
                        CONF_NAME: printer_data[CONF_NAME],
                        CONF_IP_ADDRESS: printer_data[CONF_IP_ADDRESS],
                        CONF_SERIAL_NUMBER: printer_data[CONF_SERIAL_NUMBER],
                        CONF_CHECK_CODE: printer_data[CONF_CHECK_CODE],
                    },
                    options={
                        CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
                    },
                )

            except ConnectionError:
                errors["base"] = "cannot_connect"
            except Exception as err:
                _LOGGER.exception("Unexpected error: %s", err)
                errors["base"] = "unknown"

        # Show form to enter check code
        return self.async_show_form(
            step_id="credentials",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_CHECK_CODE): cv.string,
                }
            ),
            errors=errors,
            description_placeholders={
                "name": self._printer_data.get(CONF_NAME, "Printer"),
                "ip": self._printer_data.get(CONF_IP_ADDRESS, ""),
                "serial": self._printer_data.get(CONF_SERIAL_NUMBER, ""),
            },
        )

    async def async_step_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle manual configuration."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await validate_connection(self.hass, user_input)

                # Check if already configured
                await self.async_set_unique_id(user_input[CONF_SERIAL_NUMBER])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=info["title"],
                    data={
                        CONF_NAME: user_input[CONF_NAME],
                        CONF_IP_ADDRESS: user_input[CONF_IP_ADDRESS],
                        CONF_SERIAL_NUMBER: user_input[CONF_SERIAL_NUMBER],
                        CONF_CHECK_CODE: user_input[CONF_CHECK_CODE],
                    },
                    options={
                        CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
                    },
                )

            except ConnectionError:
                errors["base"] = "cannot_connect"
            except Exception as err:
                _LOGGER.exception("Unexpected error: %s", err)
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="manual",
            data_schema=STEP_MANUAL_DATA_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> FlashForgeOptionsFlowHandler:
        """Get the options flow for this handler."""
        return FlashForgeOptionsFlowHandler(config_entry)


class FlashForgeOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for FlashForge integration."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_SCAN_INTERVAL,
                        default=self.config_entry.options.get(
                            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=5, max=300)),
                }
            ),
        )
