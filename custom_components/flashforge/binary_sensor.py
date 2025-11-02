"""Binary sensor platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge.models import FFMachineInfo, MachineState

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Describes FlashForge binary sensor entity."""

    value_fn: Callable[[FFMachineInfo], bool] | None = None


BINARY_SENSORS: tuple[FlashForgeBinarySensorEntityDescription, ...] = (
    FlashForgeBinarySensorEntityDescription(
        key="is_printing",
        name="Printing",
        device_class=BinarySensorDeviceClass.RUNNING,
        icon="mdi:printer-3d-nozzle",
        value_fn=lambda data: data.machine_state == MachineState.PRINTING,
    ),
    FlashForgeBinarySensorEntityDescription(
        key="is_online",
        name="Online",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        icon="mdi:network",
        value_fn=lambda data: True,  # If we have data, printer is online
    ),
    FlashForgeBinarySensorEntityDescription(
        key="has_error",
        name="Error",
        device_class=BinarySensorDeviceClass.PROBLEM,
        icon="mdi:alert-circle",
        value_fn=lambda data: data.machine_state == MachineState.ERROR,
    ),
    FlashForgeBinarySensorEntityDescription(
        key="is_paused",
        name="Paused",
        icon="mdi:pause-circle",
        value_fn=lambda data: data.machine_state == MachineState.PAUSED,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge binary sensors from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities = [
        FlashForgeBinarySensor(coordinator, description, printer_name, entry.entry_id)
        for description in BINARY_SENSORS
    ]

    async_add_entities(entities)


class FlashForgeBinarySensor(
    CoordinatorEntity[FlashForgeDataUpdateCoordinator], BinarySensorEntity
):
    """Representation of a FlashForge binary sensor."""

    entity_description: FlashForgeBinarySensorEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        description: FlashForgeBinarySensorEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self.entity_description = description
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
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        if self.coordinator.data is None:
            return None

        if self.entity_description.value_fn:
            return self.entity_description.value_fn(self.coordinator.data)

        return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        # is_online sensor should always report availability based on connection
        if self.entity_description.key == "is_online":
            return self.coordinator.last_update_success

        return self.coordinator.last_update_success and self.coordinator.data is not None
