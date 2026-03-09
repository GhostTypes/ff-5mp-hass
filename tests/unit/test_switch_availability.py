"""Unit tests for switch availability behavior."""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.switch import SWITCHES


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


@pytest.mark.unit
def test_camera_switch_availability_uses_pro_detection():
    """Camera switch availability should still depend on the client Pro flag."""
    camera_switch = _switch_by_key("camera")
    client = Mock()
    client.is_pro = False

    assert camera_switch.availability_fn(client) is False

    client.is_pro = True
    assert camera_switch.availability_fn(client) is True
