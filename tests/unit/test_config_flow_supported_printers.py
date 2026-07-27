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
    _is_supported_detail,
    _is_supported_discovered_printer,
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
        _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.CREATOR_5))
        is True
    )
    assert (
        _is_supported_discovered_printer(
            SimpleNamespace(model=PrinterModel.CREATOR_5_PRO)
        )
        is True
    )
    assert (
        _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.ADVENTURER_4))
        is False
    )
    assert _is_supported_discovered_printer(SimpleNamespace(model=PrinterModel.UNKNOWN)) is False


@pytest.mark.unit
def test_supported_detail_accepts_modern_printers_by_pid():
    """PID-based detection should be authoritative regardless of user-set name."""
    # PID match wins even when name is a custom value (the bug we're fixing)
    assert _is_supported_detail(SimpleNamespace(pid=35, name="LegoTech82")) is True
    assert _is_supported_detail(SimpleNamespace(pid=36, name="Workshop")) is True
    assert _is_supported_detail(SimpleNamespace(pid=38, name="Renamed")) is True
    # Creator 5 series
    assert _is_supported_detail(SimpleNamespace(pid=40, name="C5")) is True
    assert _is_supported_detail(SimpleNamespace(pid=41, name="C5 Pro")) is True
    # Legacy PIDs rejected
    assert _is_supported_detail(SimpleNamespace(pid=30, name="Whatever")) is False


@pytest.mark.unit
def test_supported_detail_accepts_the_raw_payload():
    """The gate must work on the undecoded dict, not just a parsed model.

    Reading identity from raw JSON is what keeps the supported-model check ahead
    of validation, so an unrelated bad field can no longer get a supported
    printer rejected (issue #18).
    """
    assert _is_supported_detail({"pid": 40, "name": "Creator 5", "chamberTemp": -108}) is True
    assert _is_supported_detail({"pid": 30, "name": "Adventurer 4"}) is False
    # Name fallback works on dicts too, for firmware that omits pid.
    assert _is_supported_detail({"name": "Adventurer 5M Pro"}) is True
    assert _is_supported_detail({}) is False


@pytest.mark.unit
def test_supported_detail_falls_back_to_name_when_pid_missing():
    """Firmware that omits pid should still match on name."""
    assert _is_supported_detail(SimpleNamespace(pid=None, name="Adventurer 5M")) is True
    assert _is_supported_detail(SimpleNamespace(pid=None, name="Adventurer 5M Pro")) is True
    assert _is_supported_detail(SimpleNamespace(pid=None, name="AD5X")) is True
    assert _is_supported_detail(SimpleNamespace(pid=None, name="Creator 5")) is True
    assert _is_supported_detail(SimpleNamespace(pid=None, name="Creator 5 Pro")) is True
    assert _is_supported_detail(SimpleNamespace(pid=None, name="Adventurer 4")) is False


def _make_validate_client(detail: SimpleNamespace) -> Mock:
    """Build a Mock FlashForgeClient serving ``detail`` from get_detail_raw.

    The flow reads identity from the undecoded payload, so the mock hands back a
    dict - see `_is_supported_detail`, which accepts either form.
    """
    machine_info = SimpleNamespace(name=detail.name)
    client = Mock()
    client.info.get_detail_raw = AsyncMock(
        return_value={"code": 0, "detail": {"pid": detail.pid, "name": detail.name}}
    )
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock()
    client.send_product_command = AsyncMock(return_value=True)
    client._http_session = None
    return client


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_connection_rejects_legacy_printers():
    """Manual/discovery setup should reject unsupported legacy printers."""
    client = _make_validate_client(
        SimpleNamespace(pid=30, name="Adventurer 4")
    )

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

    client.send_product_command.assert_not_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_validate_connection_accepts_renamed_5m_by_pid():
    """A 5M with a custom name (the issue #13 case) should be accepted via pid."""
    client = _make_validate_client(
        SimpleNamespace(pid=35, name="LegoTech82")
    )

    with patch("custom_components.flashforge.config_flow.FlashForgeClient", return_value=client):
        result = await validate_connection(
            Mock(),
            {
                CONF_NAME: "Workshop Printer",
                CONF_IP_ADDRESS: "192.168.3.10",
                "serial_number": "SN123456",
                "check_code": "12345678",
            },
        )

    assert result == {
        "title": "Workshop Printer",
        "machine_name": "LegoTech82",
    }
    client.send_product_command.assert_awaited_once()
