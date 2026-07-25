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


async def _run_setup(entry_options: dict):
    """Run async_setup_entry with mocked collaborators; return (result, mocks)."""
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
    entry.options = entry_options
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

    return result, {
        "hass": hass,
        "entry": entry,
        "client": client,
        "client_cls": client_cls,
        "options_cls": options_cls,
        "options_sentinel": options_sentinel,
        "machine_info": machine_info,
        "coordinator": coordinator,
    }


@pytest.mark.unit
@pytest.mark.asyncio
async def test_async_setup_entry_forces_led_capability_when_the_user_asks():
    """With the override enabled, the capability is forced on regardless of /product.

    This is the option's whole purpose: printers that report no LED but have one,
    and users who fit an aftermarket light.
    """
    result, mocks = await _run_setup(
        {
            CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
            CONF_OVERRIDE_LED_AVAILABILITY: True,
        }
    )

    assert result is True
    mocks["options_cls"].assert_called_once_with(led_control_override=True)
    mocks["client_cls"].assert_called_once_with(
        ip_address="192.168.1.100",
        serial_number="SN123456",
        check_code="CHECK123",
        options=mocks["options_sentinel"],
    )
    mocks["client"].cache_details.assert_called_once_with(mocks["machine_info"])
    mocks["client"].send_product_command.assert_awaited_once()
    mocks["coordinator"].async_config_entry_first_refresh.assert_awaited_once()
    mocks["hass"].config_entries.async_forward_entry_setups.assert_awaited_once()
    mocks["entry"].async_on_unload.assert_called_once()
    assert mocks["hass"].data[DOMAIN][mocks["entry"].entry_id]["client"] is mocks["client"]


@pytest.mark.unit
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("options", "case"),
    [
        ({CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL}, "option never set"),
        (
            {
                CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL,
                CONF_OVERRIDE_LED_AVAILABILITY: False,
            },
            "option explicitly off",
        ),
    ],
)
async def test_async_setup_entry_does_not_override_led_capability_when_off(options, case):
    """With the override off, send None - never False.

    Regression test. `led_control_override` is tri-state: None means "no
    override", but False means "force the capability OFF". The option was passed
    straight through, so every user who never touched it - the default - sent
    False and vetoed the printer's own correct capability report. The LED switch
    was greyed out on every model, and the library refused set_led_on/off
    internally, which made enabling the override look like the only way to get a
    working switch. It was: True was the only value that got past the veto.
    """
    result, mocks = await _run_setup(options)

    assert result is True, case
    mocks["options_cls"].assert_called_once_with(led_control_override=None)
