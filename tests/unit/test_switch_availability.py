"""Unit tests for switch availability behavior."""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.const import DOMAIN
from custom_components.flashforge.switch import SWITCHES
from custom_components.flashforge.switch import async_setup_entry as switch_setup_entry


def _switch_by_key(key: str):
    for switch in SWITCHES:
        if switch.key == key:
            return switch
    raise ValueError(f"Switch with key '{key}' not found")


@pytest.mark.unit
def test_led_switch_availability_uses_effective_client_capability():
    """LED switch availability should follow the effective library capability flag."""
    led_switch = _switch_by_key("led")
    client = Mock()
    client.led_control = False

    assert led_switch.availability_fn(client) is False

    client.led_control = True
    assert led_switch.availability_fn(client) is True


def _client(*, is_pro=False, is_creator5=False, is_creator5_pro=False):
    client = Mock()
    client.led_control = True
    client.is_pro = is_pro
    client.is_creator5 = is_creator5
    client.is_creator5_pro = is_creator5_pro
    return client


async def _setup_switches(client):
    hass = Mock()
    entry = Mock()
    entry.entry_id = "entry-1"
    coordinator = Mock()
    coordinator.device_model = "Printer"
    coordinator.serial_number = "SN123456"
    coordinator.firmware_version = "1.9.4"
    hass.data = {
        DOMAIN: {
            entry.entry_id: {"coordinator": coordinator, "client": client, "name": "Printer"}
        }
    }

    added = []
    await switch_setup_entry(hass, entry, added.extend)
    return {entity.entity_description.key for entity in added}


@pytest.mark.unit
def test_camera_switch_availability_uses_pro_detection():
    """Camera switch availability should depend on the Pro-model client flag."""
    camera_switch = _switch_by_key("camera")

    assert camera_switch.availability_fn(_client()) is False
    assert camera_switch.availability_fn(_client(is_pro=True)) is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_camera_switch_is_not_created_on_the_creator_5_series():
    """The Creator 5 API cannot stop the stream, so the switch must not exist.

    Confirmed on a Creator 5 Pro (firmware 1.9.4): streamCtrl_cmd reports
    success and the stream keeps serving frames, and `cameraStreamUrl` stays
    populated so the switch snaps back to `on` on the next poll. An available
    switch that silently does nothing is worse than an absent one.
    """
    assert "camera" not in await _setup_switches(_client(is_creator5=True))
    assert "camera" not in await _setup_switches(_client(is_creator5_pro=True))


@pytest.mark.unit
@pytest.mark.asyncio
async def test_camera_switch_is_still_created_on_other_models():
    """Only the Creator 5 series loses the switch; the 5M Pro keeps it."""
    assert "camera" in await _setup_switches(_client(is_pro=True))


@pytest.mark.unit
@pytest.mark.asyncio
async def test_led_switch_is_created_on_every_model():
    """Nothing else gets filtered out by the supported_fn pass."""
    assert "led" in await _setup_switches(_client(is_creator5_pro=True))
