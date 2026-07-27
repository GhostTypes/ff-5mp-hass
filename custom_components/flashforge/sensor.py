"""Sensor platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
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
from homeassistant.const import (
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    PERCENTAGE,
    EntityCategory,
    UnitOfInformation,
    UnitOfLength,
    UnitOfMass,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from homeassistant.util import dt as dt_util

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator
from .util import build_device_info

_LOGGER = logging.getLogger(__name__)

MACHINE_STATE_OPTIONS = [state.value for state in MachineState]


def _parse_disk_space_mb(raw: str | float | int | None) -> float | None:
    """Convert the library's pre-formatted disk-space value back into a float (MB)."""
    if raw is None or raw == "":
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def _completion_time(data: FFMachineInfo) -> datetime | None:
    """Return the absolute completion timestamp, rounded to the minute.

    HA 2026 rejects naive datetimes on timestamp sensors, so if the library's
    ``completion_time`` is timezone-naive we stamp it with HA's configured
    default timezone. Aware datetimes pass through unchanged.

    Timezone-stamping approach adapted from pcamp96 (GhostTypes/ff-5mp-hass#15).
    """
    if not data.estimated_time:
        return None
    if data.machine_state not in (
        MachineState.PRINTING,
        MachineState.PAUSED,
        MachineState.PAUSING,
        MachineState.HEATING,
    ):
        return None
    ts = data.completion_time
    if ts is None:
        return None
    ts = ts.replace(second=0, microsecond=0)
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=dt_util.DEFAULT_TIME_ZONE)
    return ts


def _active_ifs_slot(data: FFMachineInfo) -> int | None:
    """Return the active Material Station slot (1-4), 0 when idle, None when absent."""
    if not data.has_matl_station:
        return None
    station = getattr(data, "matl_station_info", None)
    if station is None:
        return 0
    return getattr(station, "current_slot", 0) or 0


def _is_creator5_series(data: FFMachineInfo) -> bool:
    """Creator 5 / Creator 5 Pro (4-tool tool-changer)."""
    return bool(getattr(data, "is_creator5", False) or getattr(data, "is_creator5_pro", False))


def _has_chamber(data: FFMachineInfo) -> bool:
    """True only when the printer actually reported a chamber temperature.

    The heated chamber is a Creator 5 series *option*, not a family trait.
    Gating on the model alone gave chamber-less units two entities pinned at
    0 C, because firmware reports the absent sensor as -108 rather than by
    omitting the field (issue #18). The library normalizes that sentinel away
    and sets `has_chamber_sensor` from what was actually reported.
    """
    return bool(getattr(data, "has_chamber_sensor", False))


def _has_air_quality(data: FFMachineInfo) -> bool:
    """Enclosed printers with filtration + air-quality sensor: 5M Pro and Creator 5 Pro."""
    return bool(getattr(data, "is_pro", False) or getattr(data, "is_creator5_pro", False))


def _tool_temp_value(index: int, *, target: bool = False) -> Callable[[FFMachineInfo], float]:
    """Build a value_fn for a Creator 5 per-toolhead temperature.

    ``index`` is 0-based (T0..T3). Reads ``current`` by default, ``set`` when
    ``target`` is True. Returns 0 when the per-tool array is absent or short.
    """
    attr = "set" if target else "current"

    def _fn(data: FFMachineInfo) -> float:
        tools = getattr(data, "tool_temps", None) or []
        if index < len(tools):
            return round(getattr(tools[index], attr, 0) or 0, 2)
        return 0

    return _fn


@dataclass
class FlashForgeSensorEntityDescription(SensorEntityDescription):
    """Describes FlashForge sensor entity."""

    value_fn: Callable[[FFMachineInfo], Any] | None = None
    availability_fn: Callable[[FFMachineInfo], bool] | None = None


_BASE_SENSORS: tuple[FlashForgeSensorEntityDescription, ...] = (
    FlashForgeSensorEntityDescription(
        key="machine_status",
        translation_key="machine_status",
        device_class=SensorDeviceClass.ENUM,
        options=MACHINE_STATE_OPTIONS,
        icon="mdi:printer-3d",
        value_fn=lambda data: data.machine_state.value if data.machine_state else "unknown",
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_temperature",
        translation_key="nozzle_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.extruder.current, 2) if data.extruder else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_target_temperature",
        translation_key="nozzle_target_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.extruder.set, 2) if data.extruder else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="bed_temperature",
        translation_key="bed_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.print_bed.current, 2) if data.print_bed else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="bed_target_temperature",
        translation_key="bed_target_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.print_bed.set, 2) if data.print_bed else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="print_progress",
        translation_key="print_progress",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:percent-circle",
        value_fn=lambda data: data.print_progress_int if data.print_progress_int is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="current_file",
        translation_key="current_file",
        icon="mdi:file-arrow-up-down",
        value_fn=lambda data: data.print_file_name if data.print_file_name else "None",
    ),
    FlashForgeSensorEntityDescription(
        key="current_layer",
        translation_key="current_layer",
        icon="mdi:layers",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.current_print_layer if data.current_print_layer is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="total_layers",
        translation_key="total_layers",
        icon="mdi:layers-triple",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.total_print_layers if data.total_print_layers is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="elapsed_time",
        translation_key="elapsed_time",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        icon="mdi:timer",
        value_fn=lambda data: int(data.print_duration) if data.print_duration else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="remaining_time",
        translation_key="remaining_time",
        device_class=SensorDeviceClass.DURATION,
        native_unit_of_measurement=UnitOfTime.SECONDS,
        icon="mdi:timer-sand",
        value_fn=lambda data: int(data.estimated_time) if data.estimated_time else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="print_completion_time",
        translation_key="print_completion_time",
        device_class=SensorDeviceClass.TIMESTAMP,
        icon="mdi:calendar-clock",
        value_fn=_completion_time,
    ),
    FlashForgeSensorEntityDescription(
        key="filament_length",
        translation_key="filament_length",
        device_class=SensorDeviceClass.DISTANCE,
        native_unit_of_measurement=UnitOfLength.METERS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:ruler",
        value_fn=lambda data: round(data.est_length, 2) if data.est_length else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="filament_weight",
        translation_key="filament_weight",
        device_class=SensorDeviceClass.WEIGHT,
        native_unit_of_measurement=UnitOfMass.GRAMS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:weight-gram",
        value_fn=lambda data: round(data.est_weight, 2) if data.est_weight else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="print_speed",
        translation_key="print_speed",
        icon="mdi:speedometer",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.print_speed_adjust if data.print_speed_adjust else 100,
    ),
    FlashForgeSensorEntityDescription(
        key="cooling_fan_speed",
        translation_key="cooling_fan_speed",
        icon="mdi:fan",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: int(getattr(data, "cooling_fan_speed", 0) or 0),
    ),
    FlashForgeSensorEntityDescription(
        key="chamber_fan_speed",
        translation_key="chamber_fan_speed",
        icon="mdi:fan",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: int(getattr(data, "chamber_fan_speed", 0) or 0),
        availability_fn=_has_air_quality,
    ),
    FlashForgeSensorEntityDescription(
        key="tvoc",
        translation_key="tvoc",
        device_class=SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
        native_unit_of_measurement=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:air-filter",
        value_fn=lambda data: float(getattr(data, "tvoc", 0) or 0),
        availability_fn=_has_air_quality,
    ),
    FlashForgeSensorEntityDescription(
        key="z_offset",
        translation_key="z_offset",
        icon="mdi:format-vertical-align-center",
        native_unit_of_measurement=UnitOfLength.MILLIMETERS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: round(data.z_axis_compensation, 3) if data.z_axis_compensation is not None else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="nozzle_size",
        translation_key="nozzle_size",
        icon="mdi:printer-3d-nozzle",
        value_fn=lambda data: data.nozzle_size if data.nozzle_size else "Unknown",
    ),
    FlashForgeSensorEntityDescription(
        key="filament_type",
        translation_key="filament_type",
        icon="mdi:printer-3d-nozzle-heat",
        value_fn=lambda data: data.filament_type if data.filament_type else "Unknown",
    ),
    FlashForgeSensorEntityDescription(
        key="active_ifs_slot",
        translation_key="active_ifs_slot",
        icon="mdi:tray-full",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=_active_ifs_slot,
        availability_fn=lambda data: data.has_matl_station,
    ),
    FlashForgeSensorEntityDescription(
        key="lifetime_filament",
        translation_key="lifetime_filament",
        device_class=SensorDeviceClass.DISTANCE,
        native_unit_of_measurement=UnitOfLength.METERS,
        icon="mdi:counter",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda data: round(data.cumulative_filament, 2) if data.cumulative_filament else 0,
    ),
    FlashForgeSensorEntityDescription(
        key="lifetime_runtime",
        translation_key="lifetime_runtime",
        icon="mdi:clock-outline",
        value_fn=lambda data: data.formatted_total_run_time if data.formatted_total_run_time else "0h:0m",
    ),
    FlashForgeSensorEntityDescription(
        key="firmware_version",
        translation_key="firmware_version",
        icon="mdi:chip",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data.firmware_version if data.firmware_version else None,
    ),
    FlashForgeSensorEntityDescription(
        key="ip_address",
        translation_key="ip_address",
        icon="mdi:ip-network",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: data.ip_address if data.ip_address else None,
    ),
    FlashForgeSensorEntityDescription(
        key="free_disk_space",
        translation_key="free_disk_space",
        device_class=SensorDeviceClass.DATA_SIZE,
        native_unit_of_measurement=UnitOfInformation.GIGABYTES,
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
        icon="mdi:harddisk",
        entity_category=EntityCategory.DIAGNOSTIC,
        value_fn=lambda data: _parse_disk_space_mb(data.free_disk_space),
    ),
    FlashForgeSensorEntityDescription(
        key="error_code",
        translation_key="error_code",
        icon="mdi:alert-octagon",
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
        value_fn=lambda data: data.error_code if data.error_code else None,
    ),
)


# Creator 5 series: per-toolhead temperatures (4 current + 4 target).
TOOLHEAD_SENSORS: tuple[FlashForgeSensorEntityDescription, ...] = tuple(
    FlashForgeSensorEntityDescription(
        key=f"tool_{i}_temperature",
        translation_key=f"tool_{i}_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:printer-3d-nozzle",
        value_fn=_tool_temp_value(i - 1),
        availability_fn=_is_creator5_series,
    )
    for i in range(1, 5)
) + tuple(
    FlashForgeSensorEntityDescription(
        key=f"tool_{i}_target_temperature",
        translation_key=f"tool_{i}_target_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:printer-3d-nozzle",
        value_fn=_tool_temp_value(i - 1, target=True),
        availability_fn=_is_creator5_series,
    )
    for i in range(1, 5)
)

# Heated chamber (current + target). Gated on the sensor actually reporting,
# NOT on the Creator 5 model family - the chamber is an option within that
# family, and units without it used to show two entities stuck at 0 C.
CHAMBER_SENSORS: tuple[FlashForgeSensorEntityDescription, ...] = (
    FlashForgeSensorEntityDescription(
        key="chamber_temperature",
        translation_key="chamber_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.chamber.current, 2) if data.chamber else 0,
        availability_fn=_has_chamber,
    ),
    FlashForgeSensorEntityDescription(
        key="chamber_target_temperature",
        translation_key="chamber_target_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:thermometer",
        value_fn=lambda data: round(data.chamber.set, 2) if data.chamber else 0,
        availability_fn=_has_chamber,
    ),
)

SENSORS: tuple[FlashForgeSensorEntityDescription, ...] = (
    _BASE_SENSORS + TOOLHEAD_SENSORS + CHAMBER_SENSORS
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

    async_add_entities(
        FlashForgeSensor(coordinator, description, printer_name, entry.entry_id)
        for description in SENSORS
        if description.availability_fn is None
    )

    pending = [
        description for description in SENSORS if description.availability_fn is not None
    ]

    @callback
    def _async_add_available_sensors() -> None:
        """Add capability-gated sensors as their capability first shows up.

        Deciding this once at setup strands them permanently: platform setup can
        run before the printer has reported the capability, and the first refresh
        may have failed outright. Keep watching instead.
        """
        data = coordinator.data
        if data is None:
            return
        ready = [
            description
            for description in pending
            if description.availability_fn is not None and description.availability_fn(data)
        ]
        if not ready:
            return
        for description in ready:
            pending.remove(description)
        async_add_entities(
            FlashForgeSensor(coordinator, description, printer_name, entry.entry_id)
            for description in ready
        )

    _async_add_available_sensors()
    if pending:
        entry.async_on_unload(coordinator.async_add_listener(_async_add_available_sensors))


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
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

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
