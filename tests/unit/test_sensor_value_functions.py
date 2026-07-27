"""Unit tests for sensor value extraction functions.

Tests the value_fn lambdas that transform FFMachineInfo data into sensor values.
These are pure function tests with no Home Assistant dependencies.
"""
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Mock Home Assistant modules before importing integration code
from tests.ha_mocks import mock_homeassistant
mock_homeassistant()

from custom_components.flashforge.sensor import SENSORS, _completion_time
from flashforge.models import MachineState


@pytest.mark.unit
def test_chamber_sensors_gate_on_the_sensor_not_the_model():
    """Chamber entities follow the reported sensor, not the Creator 5 badge.

    The heated chamber is an option within the Creator 5 family. Firmware on a
    unit without one reports `chamberTemp: -108` rather than omitting the field
    (issue #18); the library normalizes that away and sets `has_chamber_sensor`
    from what was actually reported. Gating on `is_creator5` gave those units
    two entities pinned at 0 C.
    """
    from custom_components.flashforge.sensor import CHAMBER_SENSORS

    chamberless_c5 = SimpleNamespace(
        is_creator5=True, is_creator5_pro=False, has_chamber_sensor=False
    )
    heated_c5 = SimpleNamespace(
        is_creator5=True, is_creator5_pro=False, has_chamber_sensor=True
    )

    assert CHAMBER_SENSORS, "expected chamber sensor descriptions"
    for description in CHAMBER_SENSORS:
        assert description.availability_fn(chamberless_c5) is False
        assert description.availability_fn(heated_c5) is True


@pytest.mark.unit
class TestSensorValueFunctions:
    """Test sensor value extraction functions."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a comprehensive mock FFMachineInfo object
        self.mock_data = Mock()

        # Machine state
        self.mock_data.machine_state = MachineState.READY

        # Temperature data (extruder and bed objects)
        self.mock_data.extruder = Mock()
        self.mock_data.extruder.current = 25.456
        self.mock_data.extruder.set = 210.789

        self.mock_data.print_bed = Mock()
        self.mock_data.print_bed.current = 22.123
        self.mock_data.print_bed.set = 60.999

        # Print job data
        self.mock_data.print_progress_int = 45
        self.mock_data.print_file_name = "test_model.gx"
        self.mock_data.current_print_layer = 150
        self.mock_data.total_print_layers = 300
        self.mock_data.print_duration = 7200  # 2 hours in seconds
        self.mock_data.print_eta = "01:30"
        self.mock_data.estimated_time = 5400  # 90 minutes remaining
        self.mock_data.cumulative_print_time = 7425  # 123h45m in minutes

        # Filament data
        self.mock_data.est_length = 1234.567
        self.mock_data.est_weight = 45.678
        self.mock_data.cumulative_filament = 50000.123

        # Printer settings
        self.mock_data.print_speed_adjust = 120
        self.mock_data.z_axis_compensation = 0.125
        self.mock_data.nozzle_size = "0.4mm"
        self.mock_data.filament_type = "PLA"

        # Lifetime stats
        self.mock_data.formatted_total_run_time = "123h:45m"

        # Device info
        self.mock_data.name = "Adventurer 5M Pro"

    def get_sensor_by_key(self, key: str):
        """Helper to get sensor description by key."""
        for sensor in SENSORS:
            if sensor.key == key:
                return sensor
        raise ValueError(f"Sensor with key '{key}' not found")

    def test_machine_status_ready(self):
        """Test machine_status sensor returns lowercase state value (translation key)."""
        sensor = self.get_sensor_by_key("machine_status")
        assert sensor.value_fn(self.mock_data) == "ready"

    def test_machine_status_printing(self):
        """Test machine_status sensor with PRINTING state."""
        self.mock_data.machine_state = MachineState.PRINTING
        sensor = self.get_sensor_by_key("machine_status")
        assert sensor.value_fn(self.mock_data) == "printing"

    def test_machine_status_none(self):
        """Test machine_status sensor handles None gracefully."""
        self.mock_data.machine_state = None
        sensor = self.get_sensor_by_key("machine_status")
        assert sensor.value_fn(self.mock_data) == "unknown"

    def test_nozzle_temperature_rounded(self):
        """Test nozzle_temperature sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("nozzle_temperature")
        assert sensor.value_fn(self.mock_data) == 25.46

    def test_nozzle_temperature_no_extruder(self):
        """Test nozzle_temperature sensor handles missing extruder."""
        self.mock_data.extruder = None
        sensor = self.get_sensor_by_key("nozzle_temperature")
        assert sensor.value_fn(self.mock_data) == 0

    def test_nozzle_target_temperature_rounded(self):
        """Test nozzle_target_temperature sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("nozzle_target_temperature")
        assert sensor.value_fn(self.mock_data) == 210.79

    def test_nozzle_target_temperature_no_extruder(self):
        """Test nozzle_target_temperature sensor handles missing extruder."""
        self.mock_data.extruder = None
        sensor = self.get_sensor_by_key("nozzle_target_temperature")
        assert sensor.value_fn(self.mock_data) == 0

    def test_bed_temperature_rounded(self):
        """Test bed_temperature sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("bed_temperature")
        assert sensor.value_fn(self.mock_data) == 22.12

    def test_bed_temperature_no_bed(self):
        """Test bed_temperature sensor handles missing bed."""
        self.mock_data.print_bed = None
        sensor = self.get_sensor_by_key("bed_temperature")
        assert sensor.value_fn(self.mock_data) == 0

    def test_bed_target_temperature_rounded(self):
        """Test bed_target_temperature sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("bed_target_temperature")
        assert sensor.value_fn(self.mock_data) == 61.0

    def test_bed_target_temperature_no_bed(self):
        """Test bed_target_temperature sensor handles missing bed."""
        self.mock_data.print_bed = None
        sensor = self.get_sensor_by_key("bed_target_temperature")
        assert sensor.value_fn(self.mock_data) == 0

    def test_print_progress(self):
        """Test print_progress sensor returns percentage."""
        sensor = self.get_sensor_by_key("print_progress")
        assert sensor.value_fn(self.mock_data) == 45

    def test_print_progress_none(self):
        """Test print_progress sensor handles None."""
        self.mock_data.print_progress_int = None
        sensor = self.get_sensor_by_key("print_progress")
        assert sensor.value_fn(self.mock_data) == 0

    def test_print_progress_zero(self):
        """Test print_progress sensor handles zero (0 is valid)."""
        self.mock_data.print_progress_int = 0
        sensor = self.get_sensor_by_key("print_progress")
        assert sensor.value_fn(self.mock_data) == 0

    def test_current_file(self):
        """Test current_file sensor returns filename."""
        sensor = self.get_sensor_by_key("current_file")
        assert sensor.value_fn(self.mock_data) == "test_model.gx"

    def test_current_file_empty(self):
        """Test current_file sensor handles empty filename."""
        self.mock_data.print_file_name = ""
        sensor = self.get_sensor_by_key("current_file")
        assert sensor.value_fn(self.mock_data) == "None"

    def test_current_file_none(self):
        """Test current_file sensor handles None."""
        self.mock_data.print_file_name = None
        sensor = self.get_sensor_by_key("current_file")
        assert sensor.value_fn(self.mock_data) == "None"

    def test_current_layer(self):
        """Test current_layer sensor returns layer number."""
        sensor = self.get_sensor_by_key("current_layer")
        assert sensor.value_fn(self.mock_data) == 150

    def test_current_layer_none(self):
        """Test current_layer sensor handles None."""
        self.mock_data.current_print_layer = None
        sensor = self.get_sensor_by_key("current_layer")
        assert sensor.value_fn(self.mock_data) == 0

    def test_current_layer_zero(self):
        """Test current_layer sensor handles zero (0 is valid)."""
        self.mock_data.current_print_layer = 0
        sensor = self.get_sensor_by_key("current_layer")
        assert sensor.value_fn(self.mock_data) == 0

    def test_total_layers(self):
        """Test total_layers sensor returns total count."""
        sensor = self.get_sensor_by_key("total_layers")
        assert sensor.value_fn(self.mock_data) == 300

    def test_total_layers_none(self):
        """Test total_layers sensor handles None."""
        self.mock_data.total_print_layers = None
        sensor = self.get_sensor_by_key("total_layers")
        assert sensor.value_fn(self.mock_data) == 0

    def test_elapsed_time(self):
        """Test elapsed_time sensor returns int seconds from print_duration."""
        sensor = self.get_sensor_by_key("elapsed_time")
        assert sensor.value_fn(self.mock_data) == 7200

    def test_elapsed_time_none(self):
        """Test elapsed_time sensor handles zero/missing print_duration."""
        self.mock_data.print_duration = 0
        sensor = self.get_sensor_by_key("elapsed_time")
        assert sensor.value_fn(self.mock_data) == 0

    def test_remaining_time(self):
        """Test remaining_time sensor returns int seconds from estimated_time."""
        sensor = self.get_sensor_by_key("remaining_time")
        assert sensor.value_fn(self.mock_data) == 5400

    def test_remaining_time_empty(self):
        """Test remaining_time sensor handles zero estimated_time."""
        self.mock_data.estimated_time = 0
        sensor = self.get_sensor_by_key("remaining_time")
        assert sensor.value_fn(self.mock_data) == 0

    def test_remaining_time_none(self):
        """Test remaining_time sensor handles None estimated_time."""
        self.mock_data.estimated_time = None
        sensor = self.get_sensor_by_key("remaining_time")
        assert sensor.value_fn(self.mock_data) == 0

    def test_filament_length_rounded(self):
        """Test filament_length sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("filament_length")
        assert sensor.value_fn(self.mock_data) == 1234.57

    def test_filament_length_none(self):
        """Test filament_length sensor handles None."""
        self.mock_data.est_length = None
        sensor = self.get_sensor_by_key("filament_length")
        assert sensor.value_fn(self.mock_data) == 0

    def test_filament_length_zero(self):
        """Test filament_length sensor handles zero (0 is falsy)."""
        self.mock_data.est_length = 0
        sensor = self.get_sensor_by_key("filament_length")
        assert sensor.value_fn(self.mock_data) == 0

    def test_filament_weight_rounded(self):
        """Test filament_weight sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("filament_weight")
        assert sensor.value_fn(self.mock_data) == 45.68

    def test_filament_weight_none(self):
        """Test filament_weight sensor handles None."""
        self.mock_data.est_weight = None
        sensor = self.get_sensor_by_key("filament_weight")
        assert sensor.value_fn(self.mock_data) == 0

    def test_print_speed(self):
        """Test print_speed sensor returns percentage."""
        sensor = self.get_sensor_by_key("print_speed")
        assert sensor.value_fn(self.mock_data) == 120

    def test_print_speed_none(self):
        """Test print_speed sensor defaults to 100."""
        self.mock_data.print_speed_adjust = None
        sensor = self.get_sensor_by_key("print_speed")
        assert sensor.value_fn(self.mock_data) == 100

    def test_print_speed_zero(self):
        """Test print_speed sensor handles zero (0 is falsy)."""
        self.mock_data.print_speed_adjust = 0
        sensor = self.get_sensor_by_key("print_speed")
        assert sensor.value_fn(self.mock_data) == 100

    def test_z_offset_rounded(self):
        """Test z_offset sensor rounds to 3 decimals."""
        sensor = self.get_sensor_by_key("z_offset")
        assert sensor.value_fn(self.mock_data) == 0.125

    def test_z_offset_negative(self):
        """Test z_offset sensor handles negative values."""
        self.mock_data.z_axis_compensation = -0.1234
        sensor = self.get_sensor_by_key("z_offset")
        assert sensor.value_fn(self.mock_data) == -0.123

    def test_z_offset_none(self):
        """Test z_offset sensor handles None."""
        self.mock_data.z_axis_compensation = None
        sensor = self.get_sensor_by_key("z_offset")
        assert sensor.value_fn(self.mock_data) == 0

    def test_z_offset_zero(self):
        """Test z_offset sensor handles zero (0 is valid)."""
        self.mock_data.z_axis_compensation = 0
        sensor = self.get_sensor_by_key("z_offset")
        assert sensor.value_fn(self.mock_data) == 0

    def test_nozzle_size(self):
        """Test nozzle_size sensor returns size string."""
        sensor = self.get_sensor_by_key("nozzle_size")
        assert sensor.value_fn(self.mock_data) == "0.4mm"

    def test_nozzle_size_empty(self):
        """Test nozzle_size sensor handles empty string."""
        self.mock_data.nozzle_size = ""
        sensor = self.get_sensor_by_key("nozzle_size")
        assert sensor.value_fn(self.mock_data) == "Unknown"

    def test_nozzle_size_none(self):
        """Test nozzle_size sensor handles None."""
        self.mock_data.nozzle_size = None
        sensor = self.get_sensor_by_key("nozzle_size")
        assert sensor.value_fn(self.mock_data) == "Unknown"

    def test_filament_type(self):
        """Test filament_type sensor returns material."""
        sensor = self.get_sensor_by_key("filament_type")
        assert sensor.value_fn(self.mock_data) == "PLA"

    def test_filament_type_empty(self):
        """Test filament_type sensor handles empty string."""
        self.mock_data.filament_type = ""
        sensor = self.get_sensor_by_key("filament_type")
        assert sensor.value_fn(self.mock_data) == "Unknown"

    def test_filament_type_none(self):
        """Test filament_type sensor handles None."""
        self.mock_data.filament_type = None
        sensor = self.get_sensor_by_key("filament_type")
        assert sensor.value_fn(self.mock_data) == "Unknown"

    def test_lifetime_filament_rounded(self):
        """Test lifetime_filament sensor rounds to 2 decimals."""
        sensor = self.get_sensor_by_key("lifetime_filament")
        assert sensor.value_fn(self.mock_data) == 50000.12

    def test_lifetime_filament_none(self):
        """Test lifetime_filament sensor handles None."""
        self.mock_data.cumulative_filament = None
        sensor = self.get_sensor_by_key("lifetime_filament")
        assert sensor.value_fn(self.mock_data) == 0

    def test_lifetime_runtime(self):
        """Test lifetime_runtime sensor returns the formatted string from the library."""
        sensor = self.get_sensor_by_key("lifetime_runtime")
        assert sensor.value_fn(self.mock_data) == "123h:45m"

    def test_lifetime_runtime_empty(self):
        """Test lifetime_runtime sensor handles empty formatted_total_run_time."""
        self.mock_data.formatted_total_run_time = ""
        sensor = self.get_sensor_by_key("lifetime_runtime")
        assert sensor.value_fn(self.mock_data) == "0h:0m"

    def test_lifetime_runtime_none(self):
        """Test lifetime_runtime sensor handles None formatted_total_run_time."""
        self.mock_data.formatted_total_run_time = None
        sensor = self.get_sensor_by_key("lifetime_runtime")
        assert sensor.value_fn(self.mock_data) == "0h:0m"

    def _setup_tool_temps(self, currents, targets=None):
        """Populate mock_data.tool_temps with Temperature-like mocks."""
        if targets is None:
            targets = currents
        self.mock_data.tool_temps = [
            Mock(current=c, set=t) for c, t in zip(currents, targets)
        ]

    def test_tool_temperatures_current(self):
        """Test per-tool current temperatures read tool_temps[i].current."""
        self._setup_tool_temps([200.0, 210.55, 0.0, 195.0])
        assert self.get_sensor_by_key("tool_1_temperature").value_fn(self.mock_data) == 200.0
        assert self.get_sensor_by_key("tool_2_temperature").value_fn(self.mock_data) == 210.55
        assert self.get_sensor_by_key("tool_4_temperature").value_fn(self.mock_data) == 195.0

    def test_tool_temperatures_target(self):
        """Test per-tool target temperatures read tool_temps[i].set."""
        self._setup_tool_temps([0, 0, 0, 0], targets=[210.0, 215.0, 0.0, 200.0])
        assert self.get_sensor_by_key("tool_2_target_temperature").value_fn(self.mock_data) == 215.0
        assert self.get_sensor_by_key("tool_4_target_temperature").value_fn(self.mock_data) == 200.0

    def test_tool_temperature_missing_array(self):
        """tool_temps absent/short returns 0 (availability gates these to C5 anyway)."""
        self.mock_data.tool_temps = None
        assert self.get_sensor_by_key("tool_1_temperature").value_fn(self.mock_data) == 0
        self._setup_tool_temps([200.0])  # only 1 tool present
        assert self.get_sensor_by_key("tool_4_temperature").value_fn(self.mock_data) == 0

    def test_chamber_temperature_rounded(self):
        """Test chamber_temperature reads chamber.current, rounded to 2 decimals."""
        self.mock_data.chamber = Mock()
        self.mock_data.chamber.current = 45.678
        self.mock_data.chamber.set = 60.0
        assert self.get_sensor_by_key("chamber_temperature").value_fn(self.mock_data) == 45.68

    def test_chamber_target_temperature(self):
        """Test chamber_target_temperature reads chamber.set."""
        self.mock_data.chamber = Mock()
        self.mock_data.chamber.current = 45.0
        self.mock_data.chamber.set = 60.5
        assert self.get_sensor_by_key("chamber_target_temperature").value_fn(self.mock_data) == 60.5

    def test_chamber_temperature_none(self):
        """chamber absent returns 0."""
        self.mock_data.chamber = None
        assert self.get_sensor_by_key("chamber_temperature").value_fn(self.mock_data) == 0

    def test_print_completion_time_adds_timezone_to_naive_datetime(self):
        """Naive completion_time gets stamped with HA's default timezone (HA 2026 fix)."""
        self.mock_data.machine_state = MachineState.PRINTING
        self.mock_data.completion_time = datetime(2026, 6, 26, 9, 47, 12)  # naive
        result = _completion_time(self.mock_data)
        assert result is not None
        assert result.tzinfo is not None
        assert result == datetime(2026, 6, 26, 9, 47, tzinfo=result.tzinfo)

    def test_print_completion_time_returns_none_when_not_printing(self):
        """Completion time is None unless actively printing/heating."""
        self.mock_data.machine_state = MachineState.READY
        self.mock_data.completion_time = datetime(2026, 6, 26, 9, 47, 12)
        assert _completion_time(self.mock_data) is None

    def test_print_completion_time_preserves_aware_datetime(self):
        """Aware datetimes pass through unchanged (tz already set)."""
        from datetime import timedelta, timezone

        self.mock_data.machine_state = MachineState.PRINTING
        aware = datetime(2026, 6, 26, 9, 47, 12, tzinfo=timezone(timedelta(hours=-5)))
        self.mock_data.completion_time = aware
        result = _completion_time(self.mock_data)
        assert result is not None
        assert result.tzinfo is aware.tzinfo

    def test_all_sensors_have_value_fn(self):
        """Verify all sensors have a value_fn defined."""
        for sensor in SENSORS:
            assert sensor.value_fn is not None, f"Sensor '{sensor.key}' missing value_fn"

    def test_sensor_count(self):
        """Verify we have the expected number of sensors."""
        assert len(SENSORS) == 38, (
            "Expected 38 sensors (28 base + 8 Creator 5 toolheads + 2 chamber)"
        )

    def test_all_sensors_have_keys(self):
        """Verify all sensors have unique keys."""
        keys = [sensor.key for sensor in SENSORS]
        assert len(keys) == len(set(keys)), "Duplicate sensor keys found"

    def test_all_sensors_have_translation_keys(self):
        """Verify all sensors declare a translation_key."""
        for sensor in SENSORS:
            assert sensor.translation_key, (
                f"Sensor '{sensor.key}' missing translation_key"
            )

    def test_all_sensors_have_icons(self):
        """Verify all sensors have icons."""
        for sensor in SENSORS:
            assert sensor.icon, f"Sensor '{sensor.key}' missing icon"
            assert sensor.icon.startswith("mdi:"), f"Sensor '{sensor.key}' has invalid icon format"
