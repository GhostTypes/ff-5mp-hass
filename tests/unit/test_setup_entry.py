"""Unit tests for config entry setup behavior."""

import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge import async_setup_entry
from custom_components.flashforge.const import (
    CONF_CHECK_CODE,
    CONF_OVERRIDE_LED_AVAILABILITY,
    CONF_SCAN_INTERVAL,
    CONF_SERIAL_NUMBER,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
)
from homeassistant.const import CONF_IP_ADDRESS, CONF_NAME


@pytest.mark.unit
@pytest.mark.asyncio
async def test_async_setup_entry_uses_library_led_override_option():
    """The integration should pass LED override configuration into the API client options."""
    hass = Mock()
    hass.data = {}
    hass.config_entries = Mock()
    hass.config_entries.async_forward_entry_setups = AsyncMock()

    entry = Mock()
    entry.entry_id = "entry-1"
    entry.data = {
        CONF_IP_ADDRESS: "192.168.1.100",
        CONF_SERIAL_NUMBER: "SN123456",
        CONF_CHECK_CODE: "CHECK123",
        CONF_NAME: "Workshop Printer",
    }
    entry.options = {
        CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
        CONF_OVERRIDE_LED_AVAILABILITY: True,
    }
    entry.add_update_listener = Mock(return_value=Mock())
    entry.async_on_unload = Mock()

    machine_info = Mock()
    client = Mock()
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock(return_value=True)
    client.send_product_command = AsyncMock(return_value=True)

    coordinator = Mock()
    coordinator.async_config_entry_first_refresh = AsyncMock()

    options_sentinel = object()

    with (
        patch("custom_components.flashforge.FiveMClientConnectionOptions", return_value=options_sentinel) as options_cls,
        patch("custom_components.flashforge.FlashForgeClient", return_value=client) as client_cls,
        patch("custom_components.flashforge.FlashForgeDataUpdateCoordinator", return_value=coordinator),
    ):
        result = await async_setup_entry(hass, entry)

    assert result is True
    options_cls.assert_called_once_with(led_control_override=True)
    client_cls.assert_called_once_with(
        ip_address="192.168.1.100",
        serial_number="SN123456",
        check_code="CHECK123",
        options=options_sentinel,
    )
    client.cache_details.assert_called_once_with(machine_info)
    client.send_product_command.assert_awaited_once()
    coordinator.async_config_entry_first_refresh.assert_awaited_once()
    hass.config_entries.async_forward_entry_setups.assert_awaited_once()
    entry.async_on_unload.assert_called_once()
    assert hass.data[DOMAIN][entry.entry_id]["client"] is client
