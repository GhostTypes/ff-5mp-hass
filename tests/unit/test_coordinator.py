"""Unit tests for the FlashForge data coordinator."""

import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.coordinator import FlashForgeDataUpdateCoordinator


@pytest.mark.unit
@pytest.mark.asyncio
async def test_coordinator_uses_detected_camera_stream_when_firmware_omits_url():
    """The coordinator should populate camera_stream_url from fallback detection."""
    machine_info = SimpleNamespace(camera_stream_url="")
    client = Mock()
    client.info = Mock()
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock()
    client.detect_camera_stream = AsyncMock(return_value="http://192.168.1.111:8080/?action=stream")

    coordinator = FlashForgeDataUpdateCoordinator(Mock(), client, "Printer", 10)

    result = await coordinator._async_update_data()

    client.cache_details.assert_called_once_with(machine_info)
    client.detect_camera_stream.assert_awaited_once()
    assert result.camera_stream_url == "http://192.168.1.111:8080/?action=stream"


@pytest.mark.unit
@pytest.mark.asyncio
async def test_coordinator_skips_camera_detection_when_firmware_reports_stream():
    """The coordinator should not probe when firmware already reports a camera URL."""
    machine_info = SimpleNamespace(camera_stream_url="http://192.168.1.120:8080/?action=stream")
    client = Mock()
    client.info = Mock()
    client.info.get = AsyncMock(return_value=machine_info)
    client.cache_details = Mock()
    client.detect_camera_stream = AsyncMock(return_value="http://192.168.1.111:8080/?action=stream")

    coordinator = FlashForgeDataUpdateCoordinator(Mock(), client, "Printer", 10)

    result = await coordinator._async_update_data()

    client.cache_details.assert_called_once_with(machine_info)
    client.detect_camera_stream.assert_not_awaited()
    assert result.camera_stream_url == "http://192.168.1.120:8080/?action=stream"
