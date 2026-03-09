"""Unit tests for modern-printer filtering in the config flow."""

import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch
from unittest.mock import MagicMock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()
sys.modules["voluptuous"] = MagicMock()

from custom_components.flashforge.config_flow import (
    UnsupportedPrinterError,
    _is_supported_discovered_printer,
    _is_supported_machine_info,
    validate_connection,
)
from flashforge.discovery import PrinterModel
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME


@pytest.mark.unit
def test_supported_discovered_printer_models_are_allowed():
    """The config flow should allow only supported modern discovery models."""
    assert _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.AD5X)) is True
    assert (
        _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.ADVENTURER_5M))
        is True
    )
    assert (
        _is_supported_discovered_printer(
            SimpleNamespace(model=PrinterModel.ADVENTURER_5M_PRO)
        )
        is True
    )
    assert (
        _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.ADVENTURER_4))
        is False
    )
    assert _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.UNKNOWN)) is False


@pytest.mark.unit
def test_supported_machine_info_accepts_modern_printers():
    """HTTP machine info should accept the supported modern printer families."""
    assert _is_supported_machine_info(SimpleNamespace(name="AD5X", is_ad5x=True)) is True
    assert (
        _is_supported_machine_info(
            SimpleNamespace(name="Adventurer 5M", is_ad5x=False)
        )
        is True
    )
    assert (
        _is_supported_machine_info(
            SimpleNamespace(name="Adventurer 5M Pro", is_ad5x=False)
        )
        is True
    )
    assert (
        _is_supported_machine_info(
            SimpleNamespace(name="Adventurer 4", is_ad5x=False)
        )
        is False
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_connection_rejects_legacy_printers():
    """Manual/discovery setup should reject unsupported legacy printers."""
    machine_info = SimpleNamespace(name="Adventurer 4", is_ad5x=False)
    client = Mock()
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock()
    client.send_product_command = AsyncMock(return_value=True)
    client._http_session = None

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        with pytest.raises(UnsupportedPrinterError):
            await validate_connection(
                Mock(),
                {
                    CONF_NAME: "Legacy Printer",
                    CONF_IP_ADDRESS: "192.168.1.50",
                    "serial_number": "LEGACY123",
                    "check_code": "12345678",
                },
            )

    client.cache_details.assert_called_once_with(machine_info)
    client.send_product_command.assert_not_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_connection_accepts_supported_modern_printer():
    """Manual/discovery setup should accept supported modern printers."""
    machine_info = SimpleNamespace(name="Adventurer 5M Pro", is_ad5x=False)
    client = Mock()
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock()
    client.send_product_command = AsyncMock(return_value=True)
    client._http_session = None

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        result = await validate_connection(
            Mock(),
            {
                CONF_NAME: "Workshop Printer",
                CONF_IP_ADDRESS: "192.168.1.100",
                "serial_number": "SN123456",
                "check_code": "12345678",
            },
        )

    assert result == {
        "title": "Workshop Printer",
        "machine_name": "Adventurer 5M Pro",
    }
    client.cache_details.assert_called_once_with(machine_info)
    client.send_product_command.assert_awaited_once()
