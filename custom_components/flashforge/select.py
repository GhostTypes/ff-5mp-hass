"""Select platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge import FlashForgeClient
from flashforge.models import FFMachineInfo

from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeSelectEntityDescription(SelectEntityDescription):
    """Describes FlashForge select entity."""

    current_fn: Callable[[FFMachineInfo], str | None] | None = None
    select_fn: Callable[[FlashForgeClient, str], Any] | None = None
    availability_fn: Callable[[FlashForgeClient], bool] | None = None


SELECTS: tuple[FlashForgeSelectEntityDescription, ...] = (
    FlashForgeSelectEntityDescription(
        key="filtration_mode",
        name="Filtration Mode",
        icon="mdi:air-filter",
        options=["Off", "Internal", "External"],
        current_fn=lambda data: (
            "External" if getattr(data, "external_fan_on", False)
            else "Internal" if getattr(data, "internal_fan_on", False)
            else "Off"
        ),
        select_fn=lambda client, option: (
            client.control.set_external_filtration_on() if option == "External"
            else client.control.set_internal_filtration_on() if option == "Internal"
            else client.control.set_filtration_off()
        ),
        availability_fn=lambda client: client.filtration_control,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge select entities from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    client: FlashForgeClient = hass.data[DOMAIN][entry.entry_id]["client"]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities = [
        FlashForgeSelect(coordinator, client, description, printer_name, entry.entry_id)
        for description in SELECTS
    ]

    async_add_entities(entities)


class FlashForgeSelect(CoordinatorEntity[FlashForgeDataUpdateCoordinator], SelectEntity):
    """Representation of a FlashForge select entity."""

    entity_description: FlashForgeSelectEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        client: FlashForgeClient,
        description: FlashForgeSelectEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the select entity."""
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
    def current_option(self) -> str | None:
        """Return the current selected option."""
        if self.coordinator.data is None:
            return None

        if self.entity_description.current_fn:
            return self.entity_description.current_fn(self.coordinator.data)

        return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if not self.coordinator.last_update_success or self.coordinator.data is None:
            return False

        # Check if this feature is available on the printer
        if self.entity_description.availability_fn:
            return self.entity_description.availability_fn(self._client)

        return True

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        if self.entity_description.select_fn:
            try:
                await self.entity_description.select_fn(self._client, option)
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error(
                    "Error selecting option %s for %s: %s",
                    option,
                    self.entity_description.name,
                    err,
                )
