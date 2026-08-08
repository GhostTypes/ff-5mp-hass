"""Binary sensor platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging

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
from .util import build_device_info

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Describes FlashForge binary sensor entity."""

    value_fn: Callable[[FFMachineInfo], bool] | None = None
    availability_fn: Callable[[FFMachineInfo], bool] | None = None


BINARY_SENSORS: tuple[FlashForgeBinarySensorEntityDescription, ...] = (
    FlashForgeBinarySensorEntityDescription(
        key="is_printing",
        translation_key="is_printing",
        device_class=BinarySensorDeviceClass.RUNNING,
        icon="mdi:printer-3d-nozzle",
        value_fn=lambda data: data.machine_state == MachineState.PRINTING,
    ),
    FlashForgeBinarySensorEntityDescription(
        key="is_online",
        translation_key="is_online",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        icon="mdi:network",
        value_fn=lambda data: True,  # If we have data, printer is online
    ),
    FlashForgeBinarySensorEntityDescription(
        key="has_error",
        translation_key="has_error",
        device_class=BinarySensorDeviceClass.PROBLEM,
        icon="mdi:alert-circle",
        # Two independent signals, and the printer does not always use the one
        # this sensor used to read. A Creator 5 Pro that detects a clog does not
        # enter the ERROR state: it pauses the print and fills `errorCode`
        # (observed live as `E0163` at 89% of a print, while `status` read
        # "pause"). Asking only about the state left the problem sensor silent
        # for the whole outage - the one entity whose job is to say that
        # something needs attention.
        value_fn=lambda data: (
            data.machine_state == MachineState.ERROR or bool(data.error_code)
        ),
    ),
    FlashForgeBinarySensorEntityDescription(
        key="is_paused",
        translation_key="is_paused",
        icon="mdi:pause-circle",
        value_fn=lambda data: data.machine_state == MachineState.PAUSED,
    ),
    FlashForgeBinarySensorEntityDescription(
        key="door_open",
        translation_key="door_open",
        device_class=BinarySensorDeviceClass.DOOR,
        icon="mdi:door",
        value_fn=lambda data: bool(getattr(data, "door_open", False)),
        availability_fn=lambda data: bool(getattr(data, "has_door_sensor", False)),
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
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

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

        if not self.coordinator.last_update_success or self.coordinator.data is None:
            return False

        if self.entity_description.availability_fn:
            return self.entity_description.availability_fn(self.coordinator.data)

        return True
