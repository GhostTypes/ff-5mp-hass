"""Unit tests for local print jobs: normalization, matching, and dispatch.

The matching rules here are the ones FlashForgeUI enforces in its dialog. They
are tested against this module rather than against the card because this module
is the one that decides - the card can be stale, spoofed, or skipped entirely by
a websocket client.
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

from custom_components.flashforge.job import (
    FALLBACK_COLOR,
    JobStartError,
    MaterialMatchingError,
    async_start_local_print,
    auto_match,
    color_warnings,
    file_to_dict,
    requires_material_matching,
    slots_to_list,
    validate_mappings,
)


def make_file(tools, *, name="benchy.3mf", use_matl_station=True):
    """Build a normalized file dict with the given (tool_id, material, color) tools."""
    entry = FFGcodeFileEntry(
        gcodeFileName=name,
        printingTime=6120,
        totalFilamentWeight=24.8,
        gcodeToolCnt=len(tools),
        useMatlStation=use_matl_station,
        gcodeToolDatas=[
            FFGcodeToolData(
                toolId=tool_id,
                materialName=material,
                materialColor=color,
                filamentWeight=12.0,
                slotId=slot_id,
            )
            for tool_id, material, color, slot_id in tools
        ],
    )
    return file_to_dict(entry)


def make_slots(*slots):
    """Build normalized slots from (slot_id, material, color) tuples; None = empty."""
    result = []
    for slot_id, material, color in slots:
        result.append(
            {
                "slot_id": slot_id,
                "is_empty": material is None,
                "material_name": material or "",
                "material_color": color or "",
            }
        )
    return result


@pytest.mark.unit
class TestNormalization:
    """Turning library models into the card's payloads."""

    def test_file_to_dict_reports_tools(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "PETG", "#000000", 2)])

        assert file_entry["file_name"] == "benchy.3mf"
        assert file_entry["printing_time"] == 6120
        assert file_entry["tool_count"] == 2
        assert [tool["material_name"] for tool in file_entry["tool_datas"]] == [
            "PLA",
            "PETG",
        ]

    def test_unreported_metadata_stays_none(self):
        """The Creator 5 lists bare names; absent must not become 0 / False.

        A multi-material file on a printer that reports no metadata must not be
        rendered as a confirmed single-material one.
        """
        file_entry = file_to_dict(FFGcodeFileEntry(gcodeFileName="plate.gcode"))

        assert file_entry["printing_time"] is None
        assert file_entry["total_filament_weight"] is None
        assert file_entry["tool_count"] is None
        assert file_entry["use_matl_station"] is None
        assert file_entry["tool_datas"] == []

    def test_slots_from_machine_info(self):
        machine_info = Mock()
        machine_info.matl_station_info.slot_infos = [
            Mock(slot_id=1, has_filament=True, material_name="PLA", material_color="#FF0000"),
            Mock(slot_id=2, has_filament=False, material_name="", material_color=""),
        ]

        slots = slots_to_list(machine_info)

        assert slots[0] == {
            "slot_id": 1,
            "is_empty": False,
            "material_name": "PLA",
            "material_color": "#FF0000",
        }
        assert slots[1]["is_empty"] is True

    def test_slot_with_filament_but_no_material_is_empty(self):
        """A slot we cannot name cannot be matched against, so treat it as empty."""
        machine_info = Mock()
        machine_info.matl_station_info.slot_infos = [
            Mock(slot_id=1, has_filament=True, material_name="", material_color="#FF0000"),
        ]

        assert slots_to_list(machine_info)[0]["is_empty"] is True

    def test_out_of_range_slot_ignored(self):
        """A fifth slot is a slot we ignore - the printer only accepts 1-4."""
        machine_info = Mock()
        machine_info.matl_station_info.slot_infos = [
            Mock(slot_id=5, has_filament=True, material_name="PLA", material_color="#FF0000"),
        ]

        assert slots_to_list(machine_info) == []

    def test_no_station_reports_no_slots(self):
        machine_info = Mock()
        machine_info.matl_station_info = None

        assert slots_to_list(machine_info) == []
        assert slots_to_list(None) == []


@pytest.mark.unit
class TestRequiresMaterialMatching:
    """Deciding whether the dialog has to open at all."""

    def test_needs_matching_with_tools_and_slots(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        assert requires_material_matching(file_entry, make_slots((1, "PLA", "#FF0000")))

    def test_no_station_means_no_matching(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        assert not requires_material_matching(file_entry, [])

    def test_no_tool_data_means_no_matching(self):
        file_entry = file_to_dict(FFGcodeFileEntry(gcodeFileName="plate.gcode"))
        assert not requires_material_matching(
            file_entry, make_slots((1, "PLA", "#FF0000"))
        )


@pytest.mark.unit
class TestAutoMatch:
    """The suggestion the dialog pre-fills, which the user then confirms."""

    def test_prefers_the_slicers_own_slot(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 2)])
        slots = make_slots((1, "PLA", "#00FF00"), (2, "PLA", "#0000FF"))

        assert auto_match(file_entry, slots)[0]["slot_id"] == 2

    def test_falls_back_to_a_color_match(self):
        file_entry = make_file([(0, "PLA", "#0000FF", 0)])
        slots = make_slots((1, "PLA", "#00FF00"), (2, "PLA", "#0000FF"))

        assert auto_match(file_entry, slots)[0]["slot_id"] == 2

    def test_falls_back_to_any_material_match(self):
        file_entry = make_file([(0, "PLA", "#123456", 0)])
        slots = make_slots((1, "PETG", "#00FF00"), (2, "PLA", "#0000FF"))

        assert auto_match(file_entry, slots)[0]["slot_id"] == 2

    def test_never_double_books_a_slot(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "PLA", "#00FF00", 1)])
        slots = make_slots((1, "PLA", "#FF0000"), (2, "PLA", "#00FF00"))

        matches = auto_match(file_entry, slots)

        assert sorted(match["slot_id"] for match in matches) == [1, 2]

    def test_leaves_unmatchable_tools_for_the_user(self):
        """Incomplete on purpose: the user maps the rest by hand."""
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "ABS", "#00FF00", 2)])
        slots = make_slots((1, "PLA", "#FF0000"), (2, "PETG", "#00FF00"))

        matches = auto_match(file_entry, slots)

        assert len(matches) == 1
        assert matches[0]["tool_id"] == 0

    def test_ignores_empty_slots(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, None, None), (2, "PLA", "#FF0000"))

        assert auto_match(file_entry, slots)[0]["slot_id"] == 2


@pytest.mark.unit
class TestValidateMappings:
    """The rules that actually gate a print start."""

    def test_accepts_a_complete_mapping(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "PETG", "#000000", 2)])
        slots = make_slots((1, "PLA", "#FF0000"), (2, "PETG", "#000000"))

        resolved = validate_mappings(
            file_entry,
            slots,
            [{"tool_id": 0, "slot_id": 1}, {"tool_id": 1, "slot_id": 2}],
        )

        assert [(m.tool_id, m.slot_id) for m in resolved] == [(0, 1), (1, 2)]
        assert resolved[0].material_name == "PLA"

    def test_rejects_an_incomplete_mapping(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "PETG", "#000000", 2)])
        slots = make_slots((1, "PLA", "#FF0000"), (2, "PETG", "#000000"))

        with pytest.raises(MaterialMatchingError, match="2 tool"):
            validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

    def test_rejects_a_material_mismatch(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PETG", "#FF0000"))

        with pytest.raises(MaterialMatchingError, match="Material mismatch"):
            validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

    def test_material_comparison_ignores_case_and_padding(self):
        file_entry = make_file([(0, " pla ", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#FF0000"))

        assert validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

    def test_rejects_an_empty_slot(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, None, None))

        with pytest.raises(MaterialMatchingError, match="empty"):
            validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

    def test_rejects_a_double_booked_slot(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1), (1, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#FF0000"), (2, "PLA", "#FF0000"))

        with pytest.raises(MaterialMatchingError, match="already assigned"):
            validate_mappings(
                file_entry,
                slots,
                [{"tool_id": 0, "slot_id": 1}, {"tool_id": 1, "slot_id": 1}],
            )

    def test_rejects_an_unknown_slot(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#FF0000"))

        with pytest.raises(MaterialMatchingError, match="not reported"):
            validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 3}])

    def test_rejects_a_tool_the_file_does_not_use(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#FF0000"))

        with pytest.raises(MaterialMatchingError, match="not used"):
            validate_mappings(file_entry, slots, [{"tool_id": 2, "slot_id": 1}])

    def test_client_supplied_material_and_colors_are_ignored(self):
        """The station report is the authority, not what the card echoed back."""
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#00FF00"))

        resolved = validate_mappings(
            file_entry,
            slots,
            [
                {
                    "tool_id": 0,
                    "slot_id": 1,
                    "material_name": "TITANIUM",
                    "slot_material_color": "#ABCDEF",
                }
            ],
        )

        assert resolved[0].material_name == "PLA"
        assert resolved[0].slot_material_color == "#00FF00"

    def test_unusable_colors_become_the_fallback(self):
        file_entry = make_file([(0, "PLA", "", 1)])
        slots = make_slots((1, "PLA", "not-a-color"))

        resolved = validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

        assert resolved[0].tool_material_color == FALLBACK_COLOR
        assert resolved[0].slot_material_color == FALLBACK_COLOR


@pytest.mark.unit
class TestColorWarnings:
    """Color differences warn; they never block."""

    def test_warns_when_colors_differ(self):
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        slots = make_slots((1, "PLA", "#00FF00"))

        resolved = validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

        assert len(color_warnings(resolved)) == 1

    def test_silent_when_colors_agree(self):
        file_entry = make_file([(0, "PLA", "#ff0000", 1)])
        slots = make_slots((1, "PLA", "#FF0000"))

        resolved = validate_mappings(file_entry, slots, [{"tool_id": 0, "slot_id": 1}])

        assert color_warnings(resolved) == []


def make_client(*, creator5=False, ad5x=False):
    """Build a client mock whose job-control calls all succeed."""
    client = Mock()
    client.is_creator5 = creator5
    client.is_ad5x = ad5x
    client.job_control = Mock()
    client.job_control.start_creator5_job = AsyncMock(return_value=True)
    client.job_control.start_ad5x_multi_color_job = AsyncMock(return_value=True)
    client.job_control.start_ad5x_single_color_job = AsyncMock(return_value=True)
    client.job_control.print_local_file = AsyncMock(return_value=True)
    return client


@pytest.mark.unit
class TestStartLocalPrint:
    """Each model family reaches /printGcode through its own payload."""

    @pytest.mark.asyncio
    async def test_creator5_sends_one_call_with_mappings(self):
        client = make_client(creator5=True)
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        mappings = validate_mappings(
            file_entry, make_slots((1, "PLA", "#FF0000")), [{"tool_id": 0, "slot_id": 1}]
        )

        await async_start_local_print(
            client, "benchy.3mf", leveling_before_print=True, mappings=mappings
        )

        params = client.job_control.start_creator5_job.await_args.args[0]
        assert params.file_name == "benchy.3mf"
        assert params.leveling_before_print is True
        assert len(params.material_mappings) == 1
        client.job_control.start_ad5x_multi_color_job.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_creator5_without_mappings_sends_none(self):
        """The C5 wants the key absent, not an empty list, for a single-tool file."""
        client = make_client(creator5=True)

        await async_start_local_print(client, "plate.gcode", leveling_before_print=False)

        params = client.job_control.start_creator5_job.await_args.args[0]
        assert params.material_mappings is None

    @pytest.mark.asyncio
    async def test_ad5x_uses_the_multi_color_command_with_mappings(self):
        client = make_client(ad5x=True)
        file_entry = make_file([(0, "PLA", "#FF0000", 1)])
        mappings = validate_mappings(
            file_entry, make_slots((1, "PLA", "#FF0000")), [{"tool_id": 0, "slot_id": 1}]
        )

        await async_start_local_print(
            client, "benchy.3mf", leveling_before_print=False, mappings=mappings
        )

        client.job_control.start_ad5x_multi_color_job.assert_awaited_once()
        client.job_control.start_ad5x_single_color_job.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_ad5x_uses_the_single_color_command_without_mappings(self):
        client = make_client(ad5x=True)

        await async_start_local_print(client, "plate.gcode", leveling_before_print=False)

        client.job_control.start_ad5x_single_color_job.assert_awaited_once()
        client.job_control.start_ad5x_multi_color_job.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_5m_uses_the_plain_local_print(self):
        client = make_client()

        await async_start_local_print(client, "plate.gcode", leveling_before_print=True)

        client.job_control.print_local_file.assert_awaited_once_with("plate.gcode", True)

    @pytest.mark.asyncio
    async def test_rejection_raises(self):
        client = make_client()
        client.job_control.print_local_file = AsyncMock(return_value=False)

        with pytest.raises(JobStartError, match="rejected"):
            await async_start_local_print(
                client, "plate.gcode", leveling_before_print=False
            )

    @pytest.mark.asyncio
    async def test_transport_failure_is_wrapped(self):
        client = make_client()
        client.job_control.print_local_file = AsyncMock(side_effect=OSError("no route"))

        with pytest.raises(JobStartError, match="no route"):
            await async_start_local_print(
                client, "plate.gcode", leveling_before_print=False
            )
