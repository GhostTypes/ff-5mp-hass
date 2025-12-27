"""Centralized Home Assistant module mocks for cross-platform unit testing.

This module provides mock implementations of Home Assistant modules, allowing us to:
1. Run tests on Windows without installing Home Assistant (Unix-only)
2. Keep test execution fast (no heavy dependencies)
3. Maintain consistent mocking across all test files
4. Enable rapid iteration during development

Import this module BEFORE importing any custom_components code that depends on HA.

Usage:
    import sys
    from pathlib import Path
    from tests.ha_mocks import mock_homeassistant

    # Add project root to path
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))

    # Mock HA modules before importing integration code
    mock_homeassistant()

    # Now safe to import
    from custom_components.flashforge.sensor import SENSORS
"""
import sys
from dataclasses import dataclass
from typing import Any
from unittest.mock import MagicMock


# Stub base classes for entities
class Entity:
    """Stub for homeassistant.helpers.entity.Entity."""

    pass


class CoordinatorEntity(Entity):
    """Stub for homeassistant.helpers.update_coordinator.CoordinatorEntity."""

    def __init__(self, coordinator):
        """Initialize coordinator entity."""
        self.coordinator = coordinator

    def __class_getitem__(cls, item):
        """Make class subscriptable for type hints like CoordinatorEntity[Coordinator]."""
        return cls


class SensorEntity(Entity):
    """Stub for homeassistant.components.sensor.SensorEntity."""

    pass


class BinarySensorEntity(Entity):
    """Stub for homeassistant.components.binary_sensor.BinarySensorEntity."""

    pass


class SwitchEntity(Entity):
    """Stub for homeassistant.components.switch.SwitchEntity."""

    pass


class ButtonEntity(Entity):
    """Stub for homeassistant.components.button.ButtonEntity."""

    pass


class SelectEntity(Entity):
    """Stub for homeassistant.components.select.SelectEntity."""

    pass


# Stub enum classes for device and state classes
class SensorStateClass:
    """Stub for homeassistant.components.sensor.SensorStateClass."""

    MEASUREMENT = "measurement"
    TOTAL = "total"
    TOTAL_INCREASING = "total_increasing"


class SensorDeviceClass:
    """Stub for homeassistant.components.sensor.SensorDeviceClass."""

    DURATION = "duration"
    TEMPERATURE = "temperature"
    ENERGY = "energy"
    POWER = "power"


class BinarySensorDeviceClass:
    """Stub for homeassistant.components.binary_sensor.BinarySensorDeviceClass."""

    RUNNING = "running"
    CONNECTIVITY = "connectivity"
    PROBLEM = "problem"


# Stub classes for entity descriptions (needed for dataclass inheritance)
@dataclass
class SensorEntityDescription:
    """Stub for homeassistant.components.sensor.SensorEntityDescription."""

    key: str = ""
    name: str | None = None
    icon: str | None = None
    device_class: Any | None = None
    state_class: Any | None = None
    native_unit_of_measurement: str | None = None


@dataclass
class BinarySensorEntityDescription:
    """Stub for homeassistant.components.binary_sensor.BinarySensorEntityDescription."""

    key: str = ""
    name: str | None = None
    icon: str | None = None
    device_class: Any | None = None


@dataclass
class SwitchEntityDescription:
    """Stub for homeassistant.components.switch.SwitchEntityDescription."""

    key: str = ""
    name: str | None = None
    icon: str | None = None


@dataclass
class ButtonEntityDescription:
    """Stub for homeassistant.components.button.ButtonEntityDescription."""

    key: str = ""
    name: str | None = None
    icon: str | None = None


@dataclass
class SelectEntityDescription:
    """Stub for homeassistant.components.select.SelectEntityDescription."""

    key: str = ""
    name: str | None = None
    icon: str | None = None


def mock_homeassistant():
    """Mock all Home Assistant modules required for unit testing.

    This function should be called before importing any custom_components code
    that has dependencies on Home Assistant modules.
    """
    # Core Home Assistant modules
    sys.modules["homeassistant"] = MagicMock()
    sys.modules["homeassistant.core"] = MagicMock()

    # Constants module with common values
    const_module = MagicMock()
    const_module.PERCENTAGE = "%"

    # UnitOfTime stub
    class UnitOfTime:
        SECONDS = "s"
        MINUTES = "min"
        HOURS = "h"

    const_module.UnitOfTime = UnitOfTime
    sys.modules["homeassistant.const"] = const_module

    # Config and setup
    sys.modules["homeassistant.config_entries"] = MagicMock()
    sys.modules["homeassistant.setup"] = MagicMock()
    sys.modules["homeassistant.loader"] = MagicMock()

    # Helpers
    sys.modules["homeassistant.helpers"] = MagicMock()
    sys.modules["homeassistant.helpers.entity"] = MagicMock()
    sys.modules["homeassistant.helpers.entity_platform"] = MagicMock()

    update_coordinator_module = MagicMock()
    update_coordinator_module.CoordinatorEntity = CoordinatorEntity
    sys.modules["homeassistant.helpers.update_coordinator"] = update_coordinator_module

    sys.modules["homeassistant.helpers.device_registry"] = MagicMock()
    sys.modules["homeassistant.helpers.entity_registry"] = MagicMock()
    sys.modules["homeassistant.helpers.area_registry"] = MagicMock()
    sys.modules["homeassistant.helpers.storage"] = MagicMock()
    sys.modules["homeassistant.helpers.aiohttp_client"] = MagicMock()
    sys.modules["homeassistant.helpers.typing"] = MagicMock()

    # Component platforms with entity description stubs
    sys.modules["homeassistant.components"] = MagicMock()

    sensor_module = MagicMock()
    sensor_module.SensorEntityDescription = SensorEntityDescription
    sensor_module.SensorEntity = SensorEntity
    sensor_module.SensorDeviceClass = SensorDeviceClass
    sensor_module.SensorStateClass = SensorStateClass
    sys.modules["homeassistant.components.sensor"] = sensor_module

    binary_sensor_module = MagicMock()
    binary_sensor_module.BinarySensorEntityDescription = BinarySensorEntityDescription
    binary_sensor_module.BinarySensorEntity = BinarySensorEntity
    binary_sensor_module.BinarySensorDeviceClass = BinarySensorDeviceClass
    sys.modules["homeassistant.components.binary_sensor"] = binary_sensor_module

    switch_module = MagicMock()
    switch_module.SwitchEntityDescription = SwitchEntityDescription
    switch_module.SwitchEntity = SwitchEntity
    sys.modules["homeassistant.components.switch"] = switch_module

    button_module = MagicMock()
    button_module.ButtonEntityDescription = ButtonEntityDescription
    button_module.ButtonEntity = ButtonEntity
    sys.modules["homeassistant.components.button"] = button_module

    select_module = MagicMock()
    select_module.SelectEntityDescription = SelectEntityDescription
    select_module.SelectEntity = SelectEntity
    sys.modules["homeassistant.components.select"] = select_module

    sys.modules["homeassistant.components.camera"] = MagicMock()

    # Utilities and exceptions
    sys.modules["homeassistant.util"] = MagicMock()
    sys.modules["homeassistant.exceptions"] = MagicMock()

    # Data entry flow
    sys.modules["homeassistant.data_entry_flow"] = MagicMock()


def unmock_homeassistant():
    """Remove Home Assistant mocks from sys.modules.

    Useful for cleanup in test teardown if needed, though generally not required
    since pytest isolates test modules.
    """
    ha_modules = [key for key in sys.modules.keys() if key.startswith("homeassistant")]
    for module in ha_modules:
        del sys.modules[module]
