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
from flashforge import FlashForgeResponseError
from homeassistant.helpers.update_coordinator import UpdateFailed


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


@pytest.mark.unit
@pytest.mark.asyncio
async def test_unreadable_response_is_reported_as_such_not_as_a_connection_error(caplog):
    """An unreadable payload must not be logged as a communication failure.

    Both paths still raise UpdateFailed - HA should keep retrying either way,
    since an integration update may make the payload readable. What must differ
    is the wording, because the log is where the user (and the next bug report)
    looks to tell an offline printer from a schema mismatch. See issue #18.
    """
    client = Mock()
    client.info = Mock()
    client.info.get = AsyncMock(
        side_effect=FlashForgeResponseError("chamberTemp out of range")
    )

    coordinator = FlashForgeDataUpdateCoordinator(Mock(), client, "Creator 5", 10)

    with pytest.raises(UpdateFailed) as excinfo:
        await coordinator._async_update_data()

    assert "Unreadable response" in str(excinfo.value)
    assert "Error communicating" not in str(excinfo.value)
    assert "not a connection problem" in caplog.text


@pytest.mark.unit
@pytest.mark.asyncio
async def test_transport_failures_keep_the_communication_wording(caplog):
    """The other branch is unchanged - a real outage still reads like one."""
    client = Mock()
    client.info = Mock()
    client.info.get = AsyncMock(side_effect=OSError("Network unreachable"))

    coordinator = FlashForgeDataUpdateCoordinator(Mock(), client, "Creator 5", 10)

    with pytest.raises(UpdateFailed) as excinfo:
        await coordinator._async_update_data()

    assert "Error communicating" in str(excinfo.value)
