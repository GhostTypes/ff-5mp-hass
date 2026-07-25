"""Unit tests for starting prints of files stored on the printer."""

import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.print_job import (
    async_start_local_print,
    build_material_mappings,
    needs_material_station,
)
from flashforge.models import FFGcodeFileEntry, FFGcodeToolData
from homeassistant.exceptions import HomeAssistantError, ServiceValidationError


def _tool(
    tool_id: int = 0,
    slot_id: int = 1,
    material_name: str = "PLA",
    material_color: str = "#FF0000",
) -> FFGcodeToolData:
    return FFGcodeToolData(
        filament_weight=12.5,
        material_color=material_color,
        material_name=material_name,
        slot_id=slot_id,
        tool_id=tool_id,
    )


def _file_entry(
    name: str = "benchy.3mf",
    *,
    use_matl_station: bool | None = None,
    tools: list[FFGcodeToolData] | None = None,
) -> FFGcodeFileEntry:
    return FFGcodeFileEntry(
        gcode_file_name=name,
        printing_time=3600,
        use_matl_station=use_matl_station,
        gcode_tool_datas=tools,
    )


def _machine_info(slots: list[tuple[int, str, str]] | None = None) -> Mock:
    """Build a machine info stub whose Material Station reports the given slots."""
    slot_infos = [
        Mock(slot_id=slot_id, material_name=material, material_color=color)
        for slot_id, material, color in slots or []
    ]
    return Mock(matl_station_info=Mock(slot_infos=slot_infos))


def _client(**flags) -> Mock:
    client = Mock(**{"is_creator5": False, "is_ad5x": False, **flags})
    client.job_control.start_creator5_job = AsyncMock(return_value=True)
    client.job_control.start_ad5x_multi_color_job = AsyncMock(return_value=True)
    client.job_control.start_ad5x_single_color_job = AsyncMock(return_value=True)
    client.job_control.print_local_file = AsyncMock(return_value=True)
    return client


# --------------------------------------------------------------------------- #
# Material Station mapping
# --------------------------------------------------------------------------- #


@pytest.mark.unit
def test_material_station_detection():
    """Only files sliced for the Material Station need mappings."""
    assert needs_material_station(None) is False
    assert needs_material_station(_file_entry()) is False
    assert needs_material_station(_file_entry(use_matl_station=True)) is False
    assert (
        needs_material_station(_file_entry(use_matl_station=True, tools=[_tool()]))
        is True
    )
    # A plain multi-tool file that does not use the station prints as-is.
    assert needs_material_station(_file_entry(tools=[_tool()])) is False
    # Creator 5 series: /gcodeList reports names only, so nothing is known about
    # the file. It is started as-is and the printer uses the assignment stored
    # in the file - we must not invent a mapping here.
    assert needs_material_station(FFGcodeFileEntry(
        gcode_file_name="deckel_mit_logo.3mf", printing_time=0
    )) is False


@pytest.mark.unit
def test_mapping_takes_slot_color_from_the_printer():
    """The slot color must describe the filament actually loaded in that slot."""
    file_entry = _file_entry(
        use_matl_station=True,
        tools=[_tool(tool_id=0, slot_id=2, material_color="#FF0000")],
    )
    machine_info = _machine_info([(2, "PLA", "#00FF00")])

    mapping = build_material_mappings(file_entry, machine_info)[0]

    assert mapping.tool_id == 0
    assert mapping.slot_id == 2
    assert mapping.material_name == "PLA"
    assert mapping.tool_material_color == "#FF0000"
    assert mapping.slot_material_color == "#00FF00"


@pytest.mark.unit
def test_mapping_falls_back_to_the_known_color():
    """A missing color on one side is filled in from the other."""
    file_entry = _file_entry(
        use_matl_station=True, tools=[_tool(slot_id=1, material_color="")]
    )
    machine_info = _machine_info([(1, "PETG", "#0000FF")])

    mapping = build_material_mappings(file_entry, machine_info)[0]

    assert mapping.tool_material_color == "#0000FF"
    assert mapping.slot_material_color == "#0000FF"

    # The other way round: the printer reports no slot color.
    mapping = build_material_mappings(
        _file_entry(use_matl_station=True, tools=[_tool(material_color="#ABCDEF")]),
        _machine_info([(1, "PLA", "")]),
    )[0]
    assert mapping.tool_material_color == "#ABCDEF"
    assert mapping.slot_material_color == "#ABCDEF"


@pytest.mark.unit
def test_mapping_covers_every_tool():
    """Every tool in the file gets its own mapping."""
    file_entry = _file_entry(
        use_matl_station=True,
        tools=[
            _tool(tool_id=0, slot_id=1, material_color="#111111"),
            _tool(tool_id=1, slot_id=3, material_name="PETG", material_color="#222222"),
        ],
    )
    machine_info = _machine_info([(1, "PLA", "#111111"), (3, "PETG", "#333333")])

    mappings = build_material_mappings(file_entry, machine_info)

    assert [(m.tool_id, m.slot_id) for m in mappings] == [(0, 1), (1, 3)]
    assert mappings[1].slot_material_color == "#333333"


@pytest.mark.unit
@pytest.mark.parametrize(
    "tool",
    [
        _tool(slot_id=0),  # the file has no slot assignment
        _tool(material_color=""),  # no color anywhere
        _tool(material_name=""),  # no material name
    ],
)
def test_mapping_refuses_incomplete_tool_data(tool):
    """Rather than guess, tell the user to start the print from the slicer."""
    file_entry = _file_entry(use_matl_station=True, tools=[tool])

    # A ServiceValidationError - the file cannot be printed this way, the
    # integration itself did not fail.
    with pytest.raises(ServiceValidationError):
        build_material_mappings(file_entry, _machine_info())


# --------------------------------------------------------------------------- #
# Print start dispatch
# --------------------------------------------------------------------------- #


@pytest.mark.unit
@pytest.mark.asyncio
async def test_creator5_uses_the_creator5_job_command():
    """The Creator 5 series has its own /printGcode payload shape."""
    client = _client(is_creator5=True)

    await async_start_local_print(client, "benchy.3mf", leveling_before_print=True)

    params = client.job_control.start_creator5_job.await_args.args[0]
    assert params.file_name == "benchy.3mf"
    assert params.leveling_before_print is True
    assert params.material_mappings is None
    client.job_control.print_local_file.assert_not_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_creator5_multi_material_job_sends_mappings():
    """A Material Station file is started with its per-tool mappings."""
    client = _client(is_creator5=True)
    file_entry = _file_entry(use_matl_station=True, tools=[_tool(slot_id=2)])

    await async_start_local_print(
        client,
        "benchy.3mf",
        leveling_before_print=False,
        file_entry=file_entry,
        machine_info=_machine_info([(2, "PLA", "#00FF00")]),
    )

    params = client.job_control.start_creator5_job.await_args.args[0]
    assert len(params.material_mappings) == 1
    assert params.material_mappings[0].slot_id == 2


@pytest.mark.unit
@pytest.mark.asyncio
async def test_ad5x_single_and_multi_color_paths():
    """The AD5X uses separate commands for single- and multi-color jobs."""
    client = _client(is_ad5x=True)

    await async_start_local_print(client, "benchy.3mf", leveling_before_print=False)
    client.job_control.start_ad5x_single_color_job.assert_awaited_once()

    await async_start_local_print(
        client,
        "multi.3mf",
        leveling_before_print=False,
        file_entry=_file_entry(use_matl_station=True, tools=[_tool()]),
        machine_info=_machine_info([(1, "PLA", "#00FF00")]),
    )
    client.job_control.start_ad5x_multi_color_job.assert_awaited_once()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_other_models_use_print_local_file():
    """The 5M family keeps the generic print command."""
    client = _client()

    await async_start_local_print(client, "benchy.3mf", leveling_before_print=True)

    client.job_control.print_local_file.assert_awaited_once_with("benchy.3mf", True)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_missing_file_name_is_rejected():
    """An empty file name never reaches the printer."""
    client = _client()

    with pytest.raises(ServiceValidationError):
        await async_start_local_print(client, "   ", leveling_before_print=False)

    client.job_control.print_local_file.assert_not_awaited()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_rejected_print_raises():
    """A printer that declines the job must surface an error to the user."""
    client = _client()
    client.job_control.print_local_file = AsyncMock(return_value=False)

    # Not a ServiceValidationError: the call was valid, the printer refused it.
    with pytest.raises(HomeAssistantError) as err:
        await async_start_local_print(client, "benchy.3mf", leveling_before_print=False)
    assert not isinstance(err.value, ServiceValidationError)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_transport_errors_are_wrapped():
    """Library exceptions are translated into HA errors."""
    client = _client()
    client.job_control.print_local_file = AsyncMock(side_effect=OSError("no route"))

    with pytest.raises(HomeAssistantError):
        await async_start_local_print(client, "benchy.3mf", leveling_before_print=False)
