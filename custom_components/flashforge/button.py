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
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeButtonEntityDescription(ButtonEntityDescription):
    """Describes FlashForge button entity."""

    press_fn: Callable[[FlashForgeClient], Any] | None = None


BUTTONS: tuple[FlashForgeButtonEntityDescription, ...] = (
    FlashForgeButtonEntityDescription(
        key="pause_print",
        name="Pause Print",
        icon="mdi:pause",
        press_fn=lambda client: client.job_control.pause_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="resume_print",
        name="Resume Print",
        icon="mdi:play",
        press_fn=lambda client: client.job_control.resume_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="cancel_print",
        name="Cancel Print",
        icon="mdi:stop",
        press_fn=lambda client: client.job_control.cancel_print_job(),
    ),
    FlashForgeButtonEntityDescription(
        key="clear_status",
        name="Clear Status",
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
    client: FlashForgeClient = hass.data[DOMAIN][entry.entry_id]["client"]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities = [
        FlashForgeButton(coordinator, client, description, printer_name, entry.entry_id)
        for description in BUTTONS
    ]

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
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": printer_name,
            "manufacturer": "FlashForge",
            "model": (
                coordinator.data.name
                if coordinator.data and getattr(coordinator.data, "name", None)
                else "Unknown"
            ),
        }

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
