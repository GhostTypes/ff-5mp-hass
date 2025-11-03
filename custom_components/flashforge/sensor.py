"""Sensor platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge.models import FFMachineInfo, MachineState

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, UnitOfTime
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeSensorEntityDescription(SensorEntityDescription):
    """Describes FlashForge sensor entity."""

    value_fn: Callable[[FFMachineInfo], Any] | None = None


SENSORS: tuple[FlashForgeSensorEntityDescription, ...] = (
    FlashForgeSensorEntityDescription(
        key="machine_status",
        name="Machine Status",
        icon="mdi:printer-3d",
        value_fn=lambda data: data.machine_state.name if data.machine_state else "UNKNOWN",
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_temperature",
        name="Nozzle Temperature",
        native_unit_of_measurement="°C",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.extruder.current, 2) if data.extruder else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_target_temperature",
        name="Nozzle Target Temperature",
        native_unit_of_measurement="°C",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.extruder.set, 2) if data.extruder else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="bed_temperature",
        name="Bed Temperature",
        native_unit_of_measurement="°C",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.print_bed.current, 2) if data.print_bed else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="bed_target_temperature",
        name="Bed Target Temperature",
        native_unit_of_measurement="°C",
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.print_bed.set, 2) if data.print_bed else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="print_progress",
        name="Print Progress",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:percent-circle",
        value_fn=lambda data: int(data.print_progress) if data.print_progress is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="current_file",
        name="Current File",
        icon="mdi:file-arrow-up-down",
        value_fn=lambda data: data.print_file_name if data.print_file_name else "None",
    ),
    FlashForgeSensorEntityDescription(
        key="current_layer",
        name="Current Layer",
        icon="mdi:layers",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.current_print_layer if data.current_print_layer is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="total_layers",
        name="Total Layers",
        icon="mdi:layers-triple",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.total_print_layers if data.total_print_layers is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="elapsed_time",
        name="Elapsed Time",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:timer",
        value_fn=lambda data: data.print_duration if data.print_duration is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="remaining_time",
        name="Remaining Time",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:timer-sand",
        value_fn=lambda data: max(0, (data.estimated_time or 0) - (data.print_duration or 0)) if data.estimated_time else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="filament_length",
        name="Filament Length",
        icon="mdi:ruler",
        native_unit_of_measurement="m",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: round(data.est_length, 2) if data.est_length else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="filament_weight",
        name="Filament Weight",
        icon="mdi:weight-gram",
        native_unit_of_measurement="g",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: round(data.est_weight, 2) if data.est_weight else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="print_speed",
        name="Print Speed",
        icon="mdi:speedometer",
        native_unit_of_measurement="%",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.print_speed_adjust if data.print_speed_adjust else 100,
    ),
    FlashForgeSensorEntityDescription(
        key="z_offset",
        name="Z-Axis Offset",
        icon="mdi:format-vertical-align-center",
        native_unit_of_measurement="mm",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: round(data.z_axis_compensation, 3) if data.z_axis_compensation is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_size",
        name="Nozzle Size",
        icon="mdi:printer-3d-nozzle",
        value_fn=lambda data: data.nozzle_size if data.nozzle_size else "Unknown",
    ),
    FlashForgeSensorEntityDescription(
        key="filament_type",
        name="Filament Type",
        icon="mdi:printer-3d-nozzle-heat",
        value_fn=lambda data: data.filament_type if data.filament_type else "Unknown",
    ),
    FlashForgeSensorEntityDescription(
        key="lifetime_filament",
        name="Lifetime Filament Usage",
        icon="mdi:counter",
        native_unit_of_measurement="m",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: round(data.cumulative_filament, 2) if data.cumulative_filament else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="lifetime_runtime",
        name="Lifetime Runtime",
        icon="mdi:clock-outline",
        value_fn=lambda data: data.formatted_total_run_time if data.formatted_total_run_time else "0h:0m",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge sensors from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities = [
        FlashForgeSensor(coordinator, description, printer_name, entry.entry_id)
        for description in SENSORS
    ]

    async_add_entities(entities)


class FlashForgeSensor(CoordinatorEntity[FlashForgeDataUpdateCoordinator], SensorEntity):
    """Representation of a FlashForge sensor."""

    entity_description: FlashForgeSensorEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        description: FlashForgeSensorEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the sensor."""
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
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        if self.coordinator.data is None:
            return None

        if self.entity_description.value_fn:
            return self.entity_description.value_fn(self.coordinator.data)

        return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self.coordinator.data is not None
