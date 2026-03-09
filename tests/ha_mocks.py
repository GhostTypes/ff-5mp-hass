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
from unittest.mock import AsyncMock, MagicMock


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


class DataUpdateCoordinator:
    """Stub for homeassistant.helpers.update_coordinator.DataUpdateCoordinator."""

    def __init__(self, hass, logger, name: str, update_interval) -> None:
        """Initialize the coordinator."""
        self.hass = hass
        self.logger = logger
        self.name = name
        self.update_interval = update_interval
        self.data = None
        self.last_update_success = True
        self.async_request_refresh = AsyncMock()

    def __class_getitem__(cls, item):
        """Make class subscriptable for type hints like DataUpdateCoordinator[Data]."""
        return cls


class UpdateFailed(Exception):
    """Stub for homeassistant.helpers.update_coordinator.UpdateFailed."""


class ConfigEntryNotReady(Exception):
    """Stub for homeassistant.exceptions.ConfigEntryNotReady."""


class ConfigEntryAuthFailed(Exception):
    """Stub for homeassistant.exceptions.ConfigEntryAuthFailed."""


class SensorEntity(Entity):
    """Stub for homeassistant.components.sensor.SensorEntity."""

    pass


class BinarySensorEntity(Entity):
    """Stub for homeassistant.components.binary_sensor.BinarySensorEntity."""

    pass


class SwitchEntity(Entity):
    """Stub for homeassistant.components.switch.SwitchEntity."""

    pass


class Camera(Entity):
    """Stub for homeassistant.components.camera.Camera."""

    pass


class MjpegCamera(Camera):
    """Stub for homeassistant.components.mjpeg.camera.MjpegCamera."""

    def __init__(
        self,
        *,
        name: str | None = None,
        mjpeg_url: str,
        still_image_url: str | None,
        authentication: str | None = None,
        username: str | None = None,
        password: str = "",
        verify_ssl: bool = True,
        unique_id: str | None = None,
        device_info: Any | None = None,
    ) -> None:
        self._attr_name = name
        self._mjpeg_url = mjpeg_url
        self._still_image_url = still_image_url
        self._authentication = authentication
        self._username = username
        self._password = password
        self._verify_ssl = verify_ssl
        if unique_id is not None:
            self._attr_unique_id = unique_id
        if device_info is not None:
            self._attr_device_info = device_info

    async def stream_source(self) -> str:
        return self._mjpeg_url

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        return b""

    async def handle_async_mjpeg_stream(self, request):
        return None


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
    options: list[str] | None = None


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
    const_module.CONF_IP_ADDRESS = "host"
    const_module.CONF_NAME = "name"
    const_module.PERCENTAGE = "%"

    class Platform:
        SENSOR = "sensor"
        BINARY_SENSOR = "binary_sensor"
        SWITCH = "switch"
        SELECT = "select"
        BUTTON = "button"
        CAMERA = "camera"

    # UnitOfTime stub
    class UnitOfTime:
        SECONDS = "s"
        MINUTES = "min"
        HOURS = "h"

    const_module.Platform = Platform
    const_module.UnitOfTime = UnitOfTime
    sys.modules["homeassistant.const"] = const_module

    # Config and setup
    config_entries_module = MagicMock()

    class ConfigFlow:
        def __init_subclass__(cls, **kwargs):
            return super().__init_subclass__()

    class OptionsFlow:
        pass

    config_entries_module.ConfigFlow = ConfigFlow
    config_entries_module.OptionsFlow = OptionsFlow
    config_entries_module.ConfigEntry = object
    sys.modules["homeassistant.config_entries"] = config_entries_module
    sys.modules["homeassistant.setup"] = MagicMock()
    sys.modules["homeassistant.loader"] = MagicMock()

    # Helpers
    sys.modules["homeassistant.helpers"] = MagicMock()
    sys.modules["homeassistant.helpers.entity"] = MagicMock()
    sys.modules["homeassistant.helpers.entity_platform"] = MagicMock()
    sys.modules["homeassistant.helpers.config_validation"] = MagicMock()

    update_coordinator_module = MagicMock()
    update_coordinator_module.CoordinatorEntity = CoordinatorEntity
    update_coordinator_module.DataUpdateCoordinator = DataUpdateCoordinator
    update_coordinator_module.UpdateFailed = UpdateFailed
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

    camera_module = MagicMock()
    camera_module.Camera = Camera
    sys.modules["homeassistant.components.camera"] = camera_module
    sys.modules["homeassistant.components.mjpeg"] = MagicMock()
    mjpeg_camera_module = MagicMock()
    mjpeg_camera_module.MjpegCamera = MjpegCamera
    sys.modules["homeassistant.components.mjpeg.camera"] = mjpeg_camera_module

    # Utilities and exceptions
    sys.modules["homeassistant.util"] = MagicMock()
    exceptions_module = MagicMock()
    exceptions_module.ConfigEntryNotReady = ConfigEntryNotReady
    exceptions_module.ConfigEntryAuthFailed = ConfigEntryAuthFailed
    sys.modules["homeassistant.exceptions"] = exceptions_module

    # Data entry flow
    sys.modules["homeassistant.data_entry_flow"] = MagicMock()

    core_module = MagicMock()

    def callback(func):
        return func

    core_module.callback = callback
    core_module.HomeAssistant = object
    sys.modules["homeassistant.core"] = core_module


def unmock_homeassistant():
    """Remove Home Assistant mocks from sys.modules.

    Useful for cleanup in test teardown if needed, though generally not required
    since pytest isolates test modules.
    """
    ha_modules = [key for key in sys.modules.keys() if key.startswith("homeassistant")]
    for module in ha_modules:
        del sys.modules[module]
