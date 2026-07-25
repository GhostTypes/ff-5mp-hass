"""Button platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge import FlashForgeClient

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    CONF_LEVELING_BEFORE_PRINT,
    DEFAULT_LEVELING_BEFORE_PRINT,
    DOMAIN,
)
from .coordinator import FlashForgeDataUpdateCoordinator, FlashForgeFileListCoordinator
from .print_job import async_start_local_print
from .util import build_device_info

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeButtonEntityDescription(ButtonEntityDescription):
    """Describes FlashForge button entity."""

    press_fn: Callable[[FlashForgeClient], Any] | None = None


BUTTONS: tuple[FlashForgeButtonEntityDescription, ...] = (
    FlashForgeButtonEntityDescription(
        key="pause_print",
        translation_key="pause_print",
        icon="mdi:pause",
        press_fn=lambda client: client.job_control.pause_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="resume_print",
        translation_key="resume_print",
        icon="mdi:play",
        press_fn=lambda client: client.job_control.resume_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="cancel_print",
        translation_key="cancel_print",
        icon="mdi:stop",
        press_fn=lambda client: client.job_control.cancel_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="clear_status",
        translation_key="clear_status",
        icon="mdi:notification-clear-all",
        press_fn=lambda client: client.job_control.clear_platform(),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge buttons from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    file_coordinator: FlashForgeFileListCoordinator = hass.data[DOMAIN][entry.entry_id][
        "file_coordinator"
    ]
    client: FlashForgeClient = hass.data[DOMAIN][entry.entry_id]["client"]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities: list[ButtonEntity] = [
        FlashForgeButton(coordinator, client, description, printer_name, entry.entry_id)
        for description in BUTTONS
    ]
    entities.append(
        FlashForgePrintSelectedFileButton(
            coordinator, file_coordinator, client, entry, printer_name
        )
    )

    async_add_entities(entities)


class FlashForgeButton(CoordinatorEntity[FlashForgeDataUpdateCoordinator], ButtonEntity):
    """Representation of a FlashForge button."""

    entity_description: FlashForgeButtonEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        client: FlashForgeClient,
        description: FlashForgeButtonEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the button."""
        super().__init__(coordinator)
        self.entity_description = description
        self._client = client
        self._attr_unique_id = f"{entry_id}_{description.key}"
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data is not None

    async def async_press(self) -> None:
        """Handle the button press."""
        if self.entity_description.press_fn:
            try:
                await self.entity_description.press_fn(self._client)
                # Request a refresh after the action
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error(
                    "Error pressing button %s: %s", self.entity_description.name, err
                )


class FlashForgePrintSelectedFileButton(
    CoordinatorEntity[FlashForgeFileListCoordinator], ButtonEntity
):
    """Starts the print of the file picked on the print file select entity."""

    _attr_has_entity_name = True
    _attr_translation_key = "print_selected_file"
    _attr_icon = "mdi:printer"

    def __init__(
        self,
        machine_coordinator: FlashForgeDataUpdateCoordinator,
        coordinator: FlashForgeFileListCoordinator,
        client: FlashForgeClient,
        entry: ConfigEntry,
        printer_name: str,
    ) -> None:
        """Initialize the print button."""
        super().__init__(coordinator)
        self._machine_coordinator = machine_coordinator
        self._client = client
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_print_selected_file"
        self._attr_device_info = build_device_info(
            machine_coordinator, printer_name, entry.entry_id
        )

    @property
    def available(self) -> bool:
        """Return if the printer is reachable.

        Deliberately not tied to the file selection: availability means "we can
        reach the device", and a button is stateless, so every write of its state
        reads as a press in the logbook. Pressing without a selection raises a
        ServiceValidationError instead.
        """
        return (
            self.coordinator.last_update_success
            and self._machine_coordinator.last_update_success
        )

    async def async_press(self) -> None:
        """Start printing the selected file."""
        selected = self.coordinator.selected_file
        if selected is None or selected not in self.coordinator.file_names:
            raise ServiceValidationError(
                "No file selected to print - pick one on the print file entity first"
            )

        leveling_before_print = self._entry.options.get(
            CONF_LEVELING_BEFORE_PRINT, DEFAULT_LEVELING_BEFORE_PRINT
        )

        await async_start_local_print(
            self._client,
            selected,
            leveling_before_print=bool(leveling_before_print),
            file_entry=self.coordinator.entry_for(selected),
            machine_info=self._machine_coordinator.data,
        )

        await self._machine_coordinator.async_request_refresh()
