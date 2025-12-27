"""Unit tests for binary sensor value extraction functions.

Tests the value_fn lambdas that determine binary sensor states from FFMachineInfo data.
These are pure function tests with no Home Assistant dependencies.
"""
import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Mock Home Assistant modules before importing integration code
from tests.ha_mocks import mock_homeassistant
mock_homeassistant()

from custom_components.flashforge.binary_sensor import BINARY_SENSORS
from flashforge.models import MachineState


@pytest.mark.unit
class TestBinarySensorValueFunctions:
    """Test binary sensor value extraction functions."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock FFMachineInfo object
        self.mock_data = Mock()
        self.mock_data.machine_state = MachineState.READY

    def get_sensor_by_key(self, key: str):
        """Helper to get binary sensor description by key."""
        for sensor in BINARY_SENSORS:
            if sensor.key == key:
                return sensor
        raise ValueError(f"Binary sensor with key '{key}' not found")

    # is_printing tests
    def test_is_printing_true_when_printing(self):
        """Test is_printing sensor returns True when PRINTING."""
        self.mock_data.machine_state = MachineState.PRINTING
        sensor = self.get_sensor_by_key("is_printing")
        assert sensor.value_fn(self.mock_data) is True

    def test_is_printing_false_when_ready(self):
        """Test is_printing sensor returns False when READY."""
        self.mock_data.machine_state = MachineState.READY
        sensor = self.get_sensor_by_key("is_printing")
        assert sensor.value_fn(self.mock_data) is False

    def test_is_printing_false_when_paused(self):
        """Test is_printing sensor returns False when PAUSED."""
        self.mock_data.machine_state = MachineState.PAUSED
        sensor = self.get_sensor_by_key("is_printing")
        assert sensor.value_fn(self.mock_data) is False

    def test_is_printing_false_when_error(self):
        """Test is_printing sensor returns False when ERROR."""
        self.mock_data.machine_state = MachineState.ERROR
        sensor = self.get_sensor_by_key("is_printing")
        assert sensor.value_fn(self.mock_data) is False

    # is_online tests
    def test_is_online_always_true(self):
        """Test is_online sensor always returns True when we have data."""
        sensor = self.get_sensor_by_key("is_online")
        assert sensor.value_fn(self.mock_data) is True

    def test_is_online_true_regardless_of_state(self):
        """Test is_online sensor returns True for any machine state."""
        sensor = self.get_sensor_by_key("is_online")

        # Test all states
        for state in [
            MachineState.READY,
            MachineState.PRINTING,
            MachineState.PAUSED,
            MachineState.ERROR,
        ]:
            self.mock_data.machine_state = state
            assert sensor.value_fn(self.mock_data) is True, f"Failed for state {state}"

    # has_error tests
    def test_has_error_true_when_error(self):
        """Test has_error sensor returns True when ERROR."""
        self.mock_data.machine_state = MachineState.ERROR
        sensor = self.get_sensor_by_key("has_error")
        assert sensor.value_fn(self.mock_data) is True

    def test_has_error_false_when_ready(self):
        """Test has_error sensor returns False when READY."""
        self.mock_data.machine_state = MachineState.READY
        sensor = self.get_sensor_by_key("has_error")
        assert sensor.value_fn(self.mock_data) is False

    def test_has_error_false_when_printing(self):
        """Test has_error sensor returns False when PRINTING."""
        self.mock_data.machine_state = MachineState.PRINTING
        sensor = self.get_sensor_by_key("has_error")
        assert sensor.value_fn(self.mock_data) is False

    def test_has_error_false_when_paused(self):
        """Test has_error sensor returns False when PAUSED."""
        self.mock_data.machine_state = MachineState.PAUSED
        sensor = self.get_sensor_by_key("has_error")
        assert sensor.value_fn(self.mock_data) is False

    # is_paused tests
    def test_is_paused_true_when_paused(self):
        """Test is_paused sensor returns True when PAUSED."""
        self.mock_data.machine_state = MachineState.PAUSED
        sensor = self.get_sensor_by_key("is_paused")
        assert sensor.value_fn(self.mock_data) is True

    def test_is_paused_false_when_ready(self):
        """Test is_paused sensor returns False when READY."""
        self.mock_data.machine_state = MachineState.READY
        sensor = self.get_sensor_by_key("is_paused")
        assert sensor.value_fn(self.mock_data) is False

    def test_is_paused_false_when_printing(self):
        """Test is_paused sensor returns False when PRINTING."""
        self.mock_data.machine_state = MachineState.PRINTING
        sensor = self.get_sensor_by_key("is_paused")
        assert sensor.value_fn(self.mock_data) is False

    def test_is_paused_false_when_error(self):
        """Test is_paused sensor returns False when ERROR."""
        self.mock_data.machine_state = MachineState.ERROR
        sensor = self.get_sensor_by_key("is_paused")
        assert sensor.value_fn(self.mock_data) is False

    # Configuration validation tests
    def test_all_binary_sensors_have_value_fn(self):
        """Verify all binary sensors have a value_fn defined."""
        for sensor in BINARY_SENSORS:
            assert (
                sensor.value_fn is not None
            ), f"Binary sensor '{sensor.key}' missing value_fn"

    def test_binary_sensor_count(self):
        """Verify we have the expected number of binary sensors."""
        assert len(BINARY_SENSORS) == 4, "Expected 4 binary sensors"

    def test_all_binary_sensors_have_keys(self):
        """Verify all binary sensors have unique keys."""
        keys = [sensor.key for sensor in BINARY_SENSORS]
        assert len(keys) == len(set(keys)), "Duplicate binary sensor keys found"

    def test_all_binary_sensors_have_names(self):
        """Verify all binary sensors have names."""
        for sensor in BINARY_SENSORS:
            assert sensor.name, f"Binary sensor '{sensor.key}' missing name"

    def test_all_binary_sensors_have_icons(self):
        """Verify all binary sensors have icons."""
        for sensor in BINARY_SENSORS:
            assert sensor.icon, f"Binary sensor '{sensor.key}' missing icon"
            assert (
                sensor.icon.startswith("mdi:")
            ), f"Binary sensor '{sensor.key}' has invalid icon format"

    def test_binary_sensors_have_device_classes(self):
        """Verify binary sensors have appropriate device classes."""
        sensor = self.get_sensor_by_key("is_printing")
        assert sensor.device_class is not None

        sensor = self.get_sensor_by_key("is_online")
        assert sensor.device_class is not None

        sensor = self.get_sensor_by_key("has_error")
        assert sensor.device_class is not None

        # is_paused may or may not have device class (icon-based is okay)

    def test_value_functions_return_bool(self):
        """Verify all value functions return boolean values."""
        for sensor in BINARY_SENSORS:
            result = sensor.value_fn(self.mock_data)
            assert isinstance(
                result, bool
            ), f"Binary sensor '{sensor.key}' value_fn did not return bool"
