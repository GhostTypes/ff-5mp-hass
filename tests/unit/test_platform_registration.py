"""Unit tests for integration platform registration."""

import sys
from pathlib import Path

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge import PLATFORMS
from homeassistant.const import Platform


@pytest.mark.unit
def test_select_platform_is_registered():
    """The filtration select platform should be loaded with the integration."""
    assert Platform.SELECT in PLATFORMS

