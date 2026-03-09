"""Unit tests for the FlashForge camera entity."""

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.camera import FlashForgeCamera


def _build_coordinator(camera_stream_url: str):
    return SimpleNamespace(
        data=SimpleNamespace(camera_stream_url=camera_stream_url),
        last_update_success=True,
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_camera_entity_uses_printer_reported_stream_url():
    """The camera entity should expose the current stream URL from coordinator data."""
    stream_url = "http://192.168.1.120:8080/?action=stream"
    coordinator = _build_coordinator(stream_url)
    camera = FlashForgeCamera(coordinator, "Printer", "entry-id")

    assert camera.available is True
    assert await camera.stream_source() == stream_url


@pytest.mark.unit
@pytest.mark.asyncio
async def test_camera_entity_becomes_unavailable_without_stream_url():
    """The camera entity should be unavailable when the printer stops reporting a stream URL."""
    coordinator = _build_coordinator("http://192.168.1.120:8080/?action=stream")
    camera = FlashForgeCamera(coordinator, "Printer", "entry-id")

    coordinator.data.camera_stream_url = ""

    assert camera.available is False
    assert await camera.async_camera_image() is None
