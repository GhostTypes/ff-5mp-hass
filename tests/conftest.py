"""Shared test fixtures for FlashForge integration tests."""
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest

# Add the project root to sys.path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def mock_flashforge_client():
    """Create a mock FlashForge client."""
    client = Mock()
    client.info = AsyncMock()
    client.control = AsyncMock()
    client.job_control = AsyncMock()
    client.led_control = True
    client.filtration_control = True
    client.close = AsyncMock()
    return client


@pytest.fixture
def mock_machine_info():
    """Create a mock FFMachineInfo response."""
    from flashforge.models import FFMachineInfo, MachineState

    return FFMachineInfo(
        machine_name="Test Printer",
        machine_type="Adventurer 5M Pro",
        machine_status=MachineState.READY,
        nozzle_temp=25.0,
        nozzle_target_temp=0.0,
        bed_temp=22.0,
        bed_target_temp=0.0,
        progress=0,
        current_file="",
        current_layer=0,
        total_layers=0,
        print_time_elapsed_minutes=0,
        print_time_remaining_minutes=0,
        filament_length_mm=0.0,
        filament_weight_g=0.0,
        print_speed_pct=100,
        z_offset_mm=0.0,
        move_mode="READY",
        nozzle_size_mm=0.4,
        filament_type="PLA"
    )


@pytest.fixture
def mock_printer_discovery():
    """Create a mock printer from discovery."""
    from flashforge.discovery import FlashForgePrinter

    return FlashForgePrinter(
        name="Test Printer",
        serial_number="TEST123456",
        ip_address="192.168.1.100"
    )


@pytest.fixture
def mock_config_entry():
    """Create a mock Home Assistant config entry."""
    entry = Mock()
    entry.entry_id = "test_entry_id"
    entry.data = {
        "host": "192.168.1.100",
        "serial_number": "TEST123456",
        "check_code": "12345678"
    }
    entry.options = {
        "scan_interval": 10
    }
    entry.unique_id = "TEST123456"
    return entry


@pytest.fixture
def mock_hass():
    """Create a mock Home Assistant instance."""
    hass = Mock()
    hass.data = {}
    hass.config_entries = Mock()
    hass.async_create_task = Mock(side_effect=lambda coro: coro)
    return hass
