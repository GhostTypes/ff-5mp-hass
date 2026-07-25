"""Unit tests for Material Station capability detection and entity gating.

Regression cover for the Creator 5 Pro (pid 41): its ``/detail`` response omits
``hasMatlStation`` entirely, so ``FFMachineInfo.has_matl_station`` is None while
``matl_station_info`` is fully populated. Gating on the raw flag hid the four
slot swatches and the active-slot sensor on exactly the models v1.3.0 meant to
enable them for.
"""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge import image as image_platform
from custom_components.flashforge import sensor as sensor_platform
from custom_components.flashforge.const import DOMAIN
from custom_components.flashforge.util import has_material_station
from flashforge.api.controls.info import MachineInfoParser
from flashforge.models.responses import FFPrinterDetail


def _station_payload() -> dict:
    """The Material Station block a real Creator 5 Pro reports."""
    return {
        "currentLoadSlot": 0,
        "currentSlot": 2,
        "slotCnt": 4,
        "stateAction": 0,
        "stateStep": 0,
        "slotInfos": [
            {"hasFilament": True, "materialColor": "#1B1B1B", "materialName": "PLA", "slotId": 1},
            {"hasFilament": True, "materialColor": "#1B1B1B", "materialName": "PETG", "slotId": 2},
            {"hasFilament": True, "materialColor": "#FFFFFF", "materialName": "PLA", "slotId": 3},
            {"hasFilament": True, "materialColor": "#805003", "materialName": "PLA", "slotId": 4},
        ],
    }


def _detail(**overrides) -> FFPrinterDetail:
    """Build a Creator 5 Pro /detail payload; note it carries no hasMatlStation."""
    payload = {"pid": 41, "model": "Creator 5 Pro", "name": "Workshop", "status": "ready"}
    payload.update(overrides)
    return FFPrinterDetail(**payload)


def _machine_info(**detail_overrides):
    """Build an FFMachineInfo the way the library does, from a /detail payload."""
    return MachineInfoParser.from_detail(_detail(**detail_overrides))


# --------------------------------------------------------------------------- #
# Capability helper
# --------------------------------------------------------------------------- #


def test_creator5_pro_reports_no_flag_but_a_populated_station():
    """The firmware sends no flag; the slot data is the real signal.

    Asserted against the raw ``FFPrinterDetail`` on purpose: whether
    ``FFMachineInfo.has_matl_station`` stays None or gets derived depends on the
    installed library version (ff-5mp-api-py derives it from >1.3.1 onward), but
    the integration must gate correctly either way.
    """
    detail = _detail(matlStationInfo=_station_payload())

    assert detail.has_matl_station is None  # the printer sends no hasMatlStation
    assert has_material_station(MachineInfoParser.from_detail(detail)) is True


def test_ad5x_flag_alone_is_enough():
    """AD5X firmware sets the flag; no station block needed."""
    assert has_material_station(Mock(has_matl_station=True, matl_station_info=None)) is True


def test_no_station_at_all():
    info = _machine_info()

    assert info.matl_station_info is None
    assert has_material_station(info) is False


def test_none_data():
    assert has_material_station(None) is False


def test_slot_count_without_slot_infos():
    """A station reporting only its size still counts as present."""
    station = Mock(slot_cnt=4, slot_infos=[])
    assert has_material_station(Mock(has_matl_station=None, matl_station_info=station)) is True


def test_empty_station_object():
    station = Mock(slot_cnt=0, slot_infos=[])
    assert has_material_station(Mock(has_matl_station=None, matl_station_info=station)) is False


def test_active_slot_sensor_reads_through_on_creator5_pro():
    """The active-slot value_fn no longer returns None because the flag is unset."""
    info = _machine_info(matlStationInfo=_station_payload())

    assert sensor_platform._active_ifs_slot(info) == 2


# --------------------------------------------------------------------------- #
# Platform setup
# --------------------------------------------------------------------------- #


class _Coordinator:
    """Minimal coordinator that can replay updates to registered listeners."""

    def __init__(self, data=None):
        self.data = data
        self.last_update_success = True
        self.device_model = "Creator 5 Pro"
        self.listeners = []

    def async_add_listener(self, update_callback):
        self.listeners.append(update_callback)
        return lambda: self.listeners.remove(update_callback)

    def push(self, data):
        """Deliver a coordinator refresh."""
        self.data = data
        for update_callback in list(self.listeners):
            update_callback()


def _setup_args(coordinator):
    hass = Mock()
    hass.data = {DOMAIN: {"entry-1": {"coordinator": coordinator, "name": "Workshop"}}}
    entry = Mock(entry_id="entry-1")

    added: list = []

    def async_add_entities(new_entities):
        added.extend(new_entities)

    return hass, entry, async_add_entities, added


@pytest.mark.asyncio
async def test_image_setup_adds_slot_swatches_for_creator5_pro():
    coordinator = _Coordinator(_machine_info(matlStationInfo=_station_payload()))
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_platform.async_setup_entry(hass, entry, async_add_entities)

    slots = [e for e in added if isinstance(e, image_platform.FlashForgeMaterialStationSlotImage)]
    assert [e._slot_id for e in slots] == [1, 2, 3, 4]
    assert [e._swatch_key() for e in slots] == [
        ("PLA", "#1B1B1B"),
        ("PETG", "#1B1B1B"),
        ("PLA", "#FFFFFF"),
        ("PLA", "#805003"),
    ]
    assert all(e.available for e in slots)
    # Nothing left to wait for, so no listener is kept around.
    assert coordinator.listeners == []


@pytest.mark.asyncio
async def test_image_setup_skips_slot_swatches_without_a_station():
    coordinator = _Coordinator(_machine_info())
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_platform.async_setup_entry(hass, entry, async_add_entities)

    assert not any(
        isinstance(e, image_platform.FlashForgeMaterialStationSlotImage) for e in added
    )


@pytest.mark.asyncio
async def test_image_setup_adds_slot_swatches_reported_late():
    """First refresh failed / had no station: the swatches still show up later."""
    coordinator = _Coordinator(None)
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_platform.async_setup_entry(hass, entry, async_add_entities)
    assert not any(
        isinstance(e, image_platform.FlashForgeMaterialStationSlotImage) for e in added
    )

    coordinator.push(_machine_info(matlStationInfo=_station_payload()))

    slots = [e for e in added if isinstance(e, image_platform.FlashForgeMaterialStationSlotImage)]
    assert len(slots) == image_platform.IFS_SLOT_COUNT

    # A further refresh must not add them a second time.
    coordinator.push(_machine_info(matlStationInfo=_station_payload()))
    assert len(
        [e for e in added if isinstance(e, image_platform.FlashForgeMaterialStationSlotImage)]
    ) == image_platform.IFS_SLOT_COUNT


@pytest.mark.asyncio
async def test_sensor_setup_adds_active_slot_sensor_for_creator5_pro():
    coordinator = _Coordinator(_machine_info(matlStationInfo=_station_payload()))
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await sensor_platform.async_setup_entry(hass, entry, async_add_entities)

    keys = [e.entity_description.key for e in added]
    assert "active_ifs_slot" in keys
    assert keys.count("active_ifs_slot") == 1


@pytest.mark.asyncio
async def test_sensor_setup_adds_active_slot_sensor_reported_late():
    coordinator = _Coordinator(None)
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await sensor_platform.async_setup_entry(hass, entry, async_add_entities)
    assert "active_ifs_slot" not in [e.entity_description.key for e in added]

    coordinator.push(_machine_info(matlStationInfo=_station_payload()))
    keys = [e.entity_description.key for e in added]
    assert keys.count("active_ifs_slot") == 1

    coordinator.push(_machine_info(matlStationInfo=_station_payload()))
    assert [e.entity_description.key for e in added].count("active_ifs_slot") == 1


@pytest.mark.asyncio
async def test_sensor_setup_omits_active_slot_sensor_without_a_station():
    coordinator = _Coordinator(_machine_info())
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await sensor_platform.async_setup_entry(hass, entry, async_add_entities)

    assert "active_ifs_slot" not in [e.entity_description.key for e in added]
