"""Unit tests for the local file list coordinator."""

import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.coordinator import FlashForgeFileListCoordinator
from flashforge.models import FFGcodeFileEntry
from homeassistant.helpers.update_coordinator import UpdateFailed


def _entry(name: str, printing_time: int = 0) -> FFGcodeFileEntry:
    return FFGcodeFileEntry(gcode_file_name=name, printing_time=printing_time)


def _coordinator(client: Mock) -> FlashForgeFileListCoordinator:
    return FlashForgeFileListCoordinator(
        hass=Mock(), client=client, name="Workshop Printer"
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_returns_files_reported_by_the_printer():
    """The coordinator surfaces the printer's recent file list."""
    client = Mock()
    client.files.get_recent_file_list = AsyncMock(
        return_value=[_entry("benchy.3mf", 3600), _entry("bracket.gcode", 900)]
    )
    coordinator = _coordinator(client)

    data = await coordinator._async_update_data()

    assert [entry.gcode_file_name for entry in data] == ["benchy.3mf", "bracket.gcode"]


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drops_entries_without_a_file_name():
    """Entries without a usable file name would break the select options."""
    client = Mock()
    client.files.get_recent_file_list = AsyncMock(
        return_value=[_entry("benchy.3mf"), _entry("")]
    )

    data = await _coordinator(client)._async_update_data()

    assert [entry.gcode_file_name for entry in data] == ["benchy.3mf"]


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_handles_a_missing_list():
    """The library returns None/[] when the printer has no files."""
    client = Mock()
    client.files.get_recent_file_list = AsyncMock(return_value=None)

    assert await _coordinator(client)._async_update_data() == []


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_wraps_errors_in_update_failed():
    """Connection problems must surface as UpdateFailed so HA retries."""
    client = Mock()
    client.files.get_recent_file_list = AsyncMock(side_effect=OSError("boom"))
    coordinator = _coordinator(client)

    with pytest.raises(UpdateFailed):
        await coordinator._async_update_data()


@pytest.mark.unit
def test_file_names_and_entry_lookup():
    """Helpers expose the file names and the metadata entry for a file."""
    coordinator = _coordinator(Mock())
    coordinator.data = [_entry("benchy.3mf", 3600), _entry("bracket.gcode", 900)]

    assert coordinator.file_names == ["benchy.3mf", "bracket.gcode"]
    assert coordinator.entry_for("bracket.gcode").printing_time == 900
    assert coordinator.entry_for("missing.gcode") is None


@pytest.mark.unit
def test_helpers_tolerate_no_data_yet():
    """Before the first successful fetch the coordinator holds no data."""
    coordinator = _coordinator(Mock())

    assert coordinator.file_names == []
    assert coordinator.entry_for("benchy.3mf") is None
    assert coordinator.selected_file is None
