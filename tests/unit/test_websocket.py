"""Unit tests for the job card's websocket commands.

The websocket schemas are Home Assistant's to apply, so these tests call the
handler bodies directly with fully-formed messages. What is being checked is the
behaviour around the schema: entry resolution, thumbnail caching, and - the one
that matters - that a client which skips the matching dialog cannot start a
multi-material print anyway.
"""
import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Mock Home Assistant modules before importing integration code
from tests.ha_mocks import mock_homeassistant
mock_homeassistant()

from flashforge.models import FFGcodeFileEntry, FFGcodeToolData

from custom_components.flashforge.const import DOMAIN
from custom_components.flashforge.websocket import (
    ws_file_thumbnail,
    ws_list_entries,
    ws_list_files,
    ws_prepare_job,
    ws_start_job,
)

ENTRY_ID = "entry-1"


def make_machine_info(slots=((1, "PLA", "#FF0000"), (2, "PETG", "#000000"))):
    """Build machine info reporting the given (slot_id, material, color) slots."""
    machine_info = Mock()
    machine_info.machine_state = Mock(value="ready")
    machine_info.matl_station_info.slot_infos = [
        Mock(
            slot_id=slot_id,
            has_filament=material is not None,
            material_name=material or "",
            material_color=color or "",
        )
        for slot_id, material, color in slots
    ]
    return machine_info


def make_file_entry(tools=((0, "PLA", "#FF0000", 1),)):
    """Build a /gcodeList entry with the given (tool, material, color, slot) tools."""
    return FFGcodeFileEntry(
        gcodeFileName="benchy.3mf",
        printingTime=6120,
        gcodeToolCnt=len(tools),
        useMatlStation=True,
        gcodeToolDatas=[
            FFGcodeToolData(
                toolId=tool_id,
                materialName=material,
                materialColor=color,
                filamentWeight=10.0,
                slotId=slot_id,
            )
            for tool_id, material, color, slot_id in tools
        ],
    )


def make_hass(*, files=None, machine_info=None, thumbnail=b"png-bytes"):
    """Build a hass mock holding one loaded FlashForge entry."""
    client = Mock()
    client.files = Mock()
    client.files.get_recent_file_list = AsyncMock(
        return_value=files if files is not None else [make_file_entry()]
    )
    client.files.get_gcode_thumbnail = AsyncMock(return_value=thumbnail)
    client.is_ad5x = True
    client.is_creator5 = False
    client.job_control = Mock()
    client.job_control.start_ad5x_multi_color_job = AsyncMock(return_value=True)
    client.job_control.start_ad5x_single_color_job = AsyncMock(return_value=True)

    coordinator = Mock()
    coordinator.data = machine_info if machine_info is not None else make_machine_info()
    coordinator.device_model = "AD5X"
    coordinator.async_request_refresh = AsyncMock()

    hass = Mock()
    hass.data = {
        DOMAIN: {
            ENTRY_ID: {
                "coordinator": coordinator,
                "client": client,
                "name": "Workshop AD5X",
            }
        }
    }
    return hass, client, coordinator


def make_connection():
    """A connection mock exposing the last result / error sent."""
    connection = Mock()
    connection.send_result = Mock()
    connection.send_error = Mock()
    return connection


def result_of(connection):
    """Return the payload passed to send_result."""
    connection.send_result.assert_called_once()
    return connection.send_result.call_args.args[1]


@pytest.mark.unit
class TestListEntries:
    """The card editor's printer picker."""

    def test_lists_loaded_printers(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        ws_list_entries(hass, connection, {"id": 1, "type": "flashforge/entries"})

        assert result_of(connection) == {
            "entries": [{"entry_id": ENTRY_ID, "title": "Workshop AD5X"}]
        }


@pytest.mark.unit
class TestListFiles:
    """The card's initial load."""

    @pytest.mark.asyncio
    async def test_returns_files_and_slots(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        await ws_list_files(hass, connection, {"id": 1, "entry_id": ENTRY_ID})

        payload = result_of(connection)
        assert payload["model"] == "AD5X"
        assert payload["files"][0]["file_name"] == "benchy.3mf"
        assert payload["has_material_station"] is True
        assert payload["machine_state"] == "ready"

    @pytest.mark.asyncio
    async def test_unknown_entry_errors(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        await ws_list_files(hass, connection, {"id": 1, "entry_id": "nope"})

        connection.send_error.assert_called_once()
        assert connection.send_error.call_args.args[1] == "entry_not_found"

    @pytest.mark.asyncio
    async def test_printer_failure_errors(self):
        hass, client, _ = make_hass()
        client.files.get_recent_file_list = AsyncMock(side_effect=OSError("no route"))
        connection = make_connection()

        await ws_list_files(hass, connection, {"id": 1, "entry_id": ENTRY_ID})

        assert connection.send_error.call_args.args[1] == "printer_error"


@pytest.mark.unit
class TestThumbnail:
    """Thumbnails are fetched once per file name and then cached."""

    @pytest.mark.asyncio
    async def test_returns_base64_and_caches(self):
        hass, client, _ = make_hass()
        message = {"id": 1, "entry_id": ENTRY_ID, "file_name": "benchy.3mf"}

        connection = make_connection()
        await ws_file_thumbnail(hass, connection, message)
        first = result_of(connection)["image"]

        connection = make_connection()
        await ws_file_thumbnail(hass, connection, message)

        assert result_of(connection)["image"] == first
        client.files.get_gcode_thumbnail.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_missing_thumbnail_is_not_an_error(self):
        hass, _, _ = make_hass(thumbnail=None)
        connection = make_connection()

        await ws_file_thumbnail(
            hass, connection, {"id": 1, "entry_id": ENTRY_ID, "file_name": "benchy.3mf"}
        )

        assert result_of(connection) == {"image": None}
        connection.send_error.assert_not_called()


@pytest.mark.unit
class TestPrepareJob:
    """What the card is told before it opens a dialog."""

    @pytest.mark.asyncio
    async def test_suggests_a_complete_mapping(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        await ws_prepare_job(
            hass, connection, {"id": 1, "entry_id": ENTRY_ID, "file_name": "benchy.3mf"}
        )

        payload = result_of(connection)
        assert payload["requires_matching"] is True
        assert payload["suggestion_complete"] is True
        assert payload["suggested_mappings"][0]["slot_id"] == 1

    @pytest.mark.asyncio
    async def test_no_station_means_no_matching(self):
        machine_info = Mock()
        machine_info.machine_state = None
        machine_info.matl_station_info = None
        hass, _, _ = make_hass(machine_info=machine_info)
        connection = make_connection()

        await ws_prepare_job(
            hass, connection, {"id": 1, "entry_id": ENTRY_ID, "file_name": "benchy.3mf"}
        )

        payload = result_of(connection)
        assert payload["requires_matching"] is False
        assert payload["suggested_mappings"] == []

    @pytest.mark.asyncio
    async def test_incomplete_suggestion_is_reported(self):
        """One tool has no compatible slot, so the user has to finish the job."""
        hass, _, _ = make_hass(
            files=[make_file_entry(((0, "PLA", "#FF0000", 1), (1, "ABS", "#00FF00", 2)))]
        )
        connection = make_connection()

        await ws_prepare_job(
            hass, connection, {"id": 1, "entry_id": ENTRY_ID, "file_name": "benchy.3mf"}
        )

        payload = result_of(connection)
        assert payload["requires_matching"] is True
        assert payload["suggestion_complete"] is False

    @pytest.mark.asyncio
    async def test_deleted_file_errors(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        await ws_prepare_job(
            hass, connection, {"id": 1, "entry_id": ENTRY_ID, "file_name": "gone.3mf"}
        )

        assert connection.send_error.call_args.args[1] == "file_not_found"


def start_message(**overrides):
    """Build a job/start message with the schema's defaults already applied."""
    message = {
        "id": 1,
        "entry_id": ENTRY_ID,
        "file_name": "benchy.3mf",
        "leveling": False,
        "material_mappings": [],
    }
    message.update(overrides)
    return message


@pytest.mark.unit
class TestStartJob:
    """Starting a print, and refusing to."""

    @pytest.mark.asyncio
    async def test_starts_with_valid_mappings(self):
        hass, client, coordinator = make_hass()
        connection = make_connection()

        await ws_start_job(
            hass,
            connection,
            start_message(material_mappings=[{"tool_id": 0, "slot_id": 1}]),
        )

        payload = result_of(connection)
        assert payload["started"] is True
        assert payload["warnings"] == []
        client.job_control.start_ad5x_multi_color_job.assert_awaited_once()
        coordinator.async_request_refresh.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_reports_color_warnings(self):
        hass, _, _ = make_hass(machine_info=make_machine_info(((1, "PLA", "#00FF00"),)))
        connection = make_connection()

        await ws_start_job(
            hass,
            connection,
            start_message(material_mappings=[{"tool_id": 0, "slot_id": 1}]),
        )

        assert len(result_of(connection)["warnings"]) == 1

    @pytest.mark.asyncio
    async def test_refuses_to_skip_matching(self):
        """A client that skips the dialog must not get a material-station print.

        Starting anyway would let the printer fall back to the slot assignment
        baked into the file, which may point at filament that is long gone.
        """
        hass, client, _ = make_hass()
        connection = make_connection()

        await ws_start_job(hass, connection, start_message())

        assert connection.send_error.call_args.args[1] == "printer_error"
        assert "matched" in connection.send_error.call_args.args[2]
        client.job_control.start_ad5x_multi_color_job.assert_not_awaited()
        client.job_control.start_ad5x_single_color_job.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_starts_without_matching_when_no_station(self):
        machine_info = Mock()
        machine_info.machine_state = None
        machine_info.matl_station_info = None
        hass, client, _ = make_hass(machine_info=machine_info)
        connection = make_connection()

        await ws_start_job(hass, connection, start_message())

        assert result_of(connection)["started"] is True
        client.job_control.start_ad5x_single_color_job.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_invalid_mapping_is_rejected(self):
        hass, client, _ = make_hass()
        connection = make_connection()

        # Slot 2 holds PETG; the file's only tool needs PLA.
        await ws_start_job(
            hass,
            connection,
            start_message(material_mappings=[{"tool_id": 0, "slot_id": 2}]),
        )

        assert "Material mismatch" in connection.send_error.call_args.args[2]
        client.job_control.start_ad5x_multi_color_job.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_deleted_file_errors(self):
        hass, _, _ = make_hass()
        connection = make_connection()

        await ws_start_job(hass, connection, start_message(file_name="gone.3mf"))

        assert connection.send_error.call_args.args[1] == "file_not_found"
