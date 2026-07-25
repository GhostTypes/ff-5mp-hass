"""Unit tests for the print file select entity and the print button."""

import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.button import FlashForgePrintSelectedFileButton
from custom_components.flashforge.const import CONF_LEVELING_BEFORE_PRINT
from custom_components.flashforge.coordinator import FlashForgeFileListCoordinator
from custom_components.flashforge.select import FlashForgeFileSelect
from flashforge.models import FFGcodeFileEntry
from homeassistant.exceptions import HomeAssistantError


def _entry(name: str, printing_time: int = 3600) -> FFGcodeFileEntry:
    return FFGcodeFileEntry(
        gcode_file_name=name,
        printing_time=printing_time,
        total_filament_weight=25.5,
        gcode_tool_cnt=1,
        use_matl_station=False,
    )


def _build(options: dict | None = None, files: list[FFGcodeFileEntry] | None = None):
    """Build a select entity, a button, and the pieces they share."""
    file_coordinator = FlashForgeFileListCoordinator(
        hass=Mock(), client=Mock(), name="Workshop Printer"
    )
    file_coordinator.data = (
        files if files is not None else [_entry("benchy.3mf"), _entry("bracket.gcode")]
    )

    machine_coordinator = Mock(data=Mock(), last_update_success=True)
    machine_coordinator.async_request_refresh = AsyncMock()

    config_entry = Mock(entry_id="entry-1", options=options or {})
    client = Mock()

    select = FlashForgeFileSelect(
        machine_coordinator, file_coordinator, client, config_entry, "Workshop Printer"
    )
    button = FlashForgePrintSelectedFileButton(
        machine_coordinator, file_coordinator, client, config_entry, "Workshop Printer"
    )
    return select, button, file_coordinator, machine_coordinator, client


# --------------------------------------------------------------------------- #
# Select entity
# --------------------------------------------------------------------------- #


@pytest.mark.unit
def test_options_list_the_files_on_the_printer():
    """The dropdown shows what the printer reported."""
    select, _, _, _, _ = _build()

    assert select.options == ["benchy.3mf", "bracket.gcode"]
    assert select.current_option is None


@pytest.mark.unit
def test_file_metadata_is_exposed_as_attributes():
    """Print time and filament weight are available for templates and cards."""
    select, _, _, _, _ = _build()

    files = select.extra_state_attributes["files"]

    assert files[0] == {
        "name": "benchy.3mf",
        "printing_time": 3600,
        "filament_weight": 25.5,
        "tool_count": 1,
        "uses_material_station": False,
    }


@pytest.mark.unit
@pytest.mark.asyncio
async def test_selecting_a_file_records_it():
    """Selecting only records the choice - it does not start a print."""
    select, button, file_coordinator, _, client = _build()

    await select.async_select_option("bracket.gcode")

    assert file_coordinator.selected_file == "bracket.gcode"
    assert select.current_option == "bracket.gcode"
    client.job_control.assert_not_called()
    # The print button's availability follows the selection, so it has to be
    # told about it right away instead of waiting for the next poll.
    file_coordinator.async_update_listeners.assert_called_once()
    assert button.available is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_selecting_an_unknown_file_is_rejected():
    """Guards against stale dashboards picking a deleted file."""
    select, _, _, _, _ = _build()

    with pytest.raises(HomeAssistantError):
        await select.async_select_option("gone.gcode")


@pytest.mark.unit
def test_selection_is_dropped_when_the_file_disappears():
    """A file deleted on the printer must not stay reported as the state."""
    select, _, file_coordinator, _, _ = _build()
    file_coordinator.selected_file = "benchy.3mf"

    file_coordinator.data = [_entry("bracket.gcode")]

    assert select.current_option is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_print_file_service_uses_the_selected_file_and_option_default():
    """Called without arguments the service prints the selection."""
    select, _, file_coordinator, machine_coordinator, client = _build(
        options={CONF_LEVELING_BEFORE_PRINT: True}
    )
    file_coordinator.selected_file = "benchy.3mf"

    with patch(
        "custom_components.flashforge.select.async_start_local_print",
        new=AsyncMock(),
    ) as start:
        await select.async_print_file()

    assert start.await_args.args == (client, "benchy.3mf")
    assert start.await_args.kwargs["leveling_before_print"] is True
    assert start.await_args.kwargs["file_entry"].gcode_file_name == "benchy.3mf"
    assert start.await_args.kwargs["machine_info"] is machine_coordinator.data
    machine_coordinator.async_request_refresh.assert_awaited_once()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_print_file_service_accepts_a_file_not_in_the_list():
    """The list only holds the printer's recent files, any name may be printed."""
    select, _, _, _, client = _build()

    with patch(
        "custom_components.flashforge.select.async_start_local_print",
        new=AsyncMock(),
    ) as start:
        await select.async_print_file("older.gcode", False)

    assert start.await_args.args == (client, "older.gcode")
    assert start.await_args.kwargs["leveling_before_print"] is False
    assert start.await_args.kwargs["file_entry"] is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_print_file_service_without_a_file_errors():
    """Nothing selected and no file name given is a user error."""
    select, _, _, _, _ = _build()

    with pytest.raises(HomeAssistantError):
        await select.async_print_file()


# --------------------------------------------------------------------------- #
# Button
# --------------------------------------------------------------------------- #


@pytest.mark.unit
def test_button_needs_a_selected_file():
    """Without a selection there is nothing to print."""
    _, button, file_coordinator, _, _ = _build()

    assert button.available is False

    file_coordinator.selected_file = "benchy.3mf"
    assert button.available is True

    # A selection that is no longer on the printer keeps the button disabled.
    file_coordinator.selected_file = "gone.gcode"
    assert button.available is False


@pytest.mark.unit
def test_button_unavailable_when_the_printer_is_unreachable():
    """Availability follows both coordinators."""
    _, button, file_coordinator, machine_coordinator, _ = _build()
    file_coordinator.selected_file = "benchy.3mf"

    machine_coordinator.last_update_success = False
    assert button.available is False

    machine_coordinator.last_update_success = True
    file_coordinator.last_update_success = False
    assert button.available is False


@pytest.mark.unit
@pytest.mark.asyncio
async def test_button_starts_the_selected_file():
    """Pressing the button prints the selected file and refreshes the state."""
    _, button, file_coordinator, machine_coordinator, client = _build(
        options={CONF_LEVELING_BEFORE_PRINT: True}
    )
    file_coordinator.selected_file = "bracket.gcode"

    with patch(
        "custom_components.flashforge.button.async_start_local_print",
        new=AsyncMock(),
    ) as start:
        await button.async_press()

    assert start.await_args.args == (client, "bracket.gcode")
    assert start.await_args.kwargs["leveling_before_print"] is True
    assert start.await_args.kwargs["file_entry"].gcode_file_name == "bracket.gcode"
    machine_coordinator.async_request_refresh.assert_awaited_once()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_button_without_a_selection_errors():
    """A press without a selection reports a clear error."""
    _, button, _, _, _ = _build()

    with pytest.raises(HomeAssistantError):
        await button.async_press()
