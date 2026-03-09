"""Unit tests for the FlashForge select entity descriptions."""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.select import SELECTS


def _select_by_key(key: str):
    for select in SELECTS:
        if select.key == key:
            return select
    raise ValueError(f"Select with key '{key}' not found")


@pytest.mark.unit
def test_filtration_select_availability_uses_client_capability():
    """Filtration select availability should follow the client capability flag."""
    filtration_select = _select_by_key("filtration_mode")
    client = Mock()
    client.filtration_control = False

    assert filtration_select.availability_fn(client) is False

    client.filtration_control = True
    assert filtration_select.availability_fn(client) is True

