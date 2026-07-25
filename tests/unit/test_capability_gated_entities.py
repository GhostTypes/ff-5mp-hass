"""Unit tests for capability-gated entity registration.

Two failure modes are covered here, both of which left a printer permanently
without entities it should have had:

1. Gating on a capability the printer reports late (or not on the first poll),
   and deciding once at setup.
2. Reading a raw ``/detail`` passthrough as a capability. ``has_matl_station``
   used to mirror the AD5X-only ``hasMatlStation`` field, which the Creator 5
   series never sends - the library derives it from the slot data now, and these
   tests pin the integration to that contract.
"""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.ha_mocks import mock_homeassistant

mock_homeassistant()

from custom_components.flashforge.const import DOMAIN
from custom_components.flashforge.image import IFS_SLOT_COUNT
from custom_components.flashforge.image import async_setup_entry as image_setup_entry
from custom_components.flashforge.sensor import async_setup_entry as sensor_setup_entry


class _FakeCoordinator:
    """Coordinator stub that can publish data after setup, like the real one."""

    def __init__(self, data=None):
        self.data = data
        self.last_update_success = True
        self.device_model = "Creator 5 Pro"  # read by build_device_info
        self.serial_number = "SN123456"
        self.firmware_version = "1.9.4"
        self._listeners = []

    def async_add_listener(self, listener):
        self._listeners.append(listener)
        return lambda: self._listeners.remove(listener)

    def publish(self, data) -> None:
        """Deliver a refresh to everyone watching."""
        self.data = data
        for listener in list(self._listeners):
            listener()


def _machine_info(*, has_matl_station: bool):
    info = Mock()
    info.has_matl_station = has_matl_station
    station = Mock()
    station.slot_infos = []
    info.matl_station_info = station if has_matl_station else None
    return info


def _setup_args(coordinator):
    hass = Mock()
    entry = Mock()
    entry.entry_id = "entry-1"
    entry.async_on_unload = Mock()
    hass.data = {DOMAIN: {entry.entry_id: {"coordinator": coordinator, "name": "Printer"}}}

    added = []

    def async_add_entities(entities):
        added.extend(entities)

    return hass, entry, async_add_entities, added


def _slot_images(added):
    return [e for e in added if "ifs_slot" in (getattr(e, "_attr_unique_id", "") or "")]


@pytest.mark.unit
@pytest.mark.asyncio
async def test_slot_images_added_when_the_station_is_present_at_setup():
    """The common case: the first refresh already showed the station."""
    coordinator = _FakeCoordinator(_machine_info(has_matl_station=True))
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_setup_entry(hass, entry, async_add_entities)

    assert len(_slot_images(added)) == IFS_SLOT_COUNT
    # Nothing to wait for, so no listener is registered.
    entry.async_on_unload.assert_not_called()


@pytest.mark.unit
@pytest.mark.asyncio
async def test_slot_images_added_when_the_station_reports_in_later():
    """A capability that shows up on a later refresh must still create entities.

    Regression test: platform setup can run before the printer has reported the
    station, and the first refresh may have failed outright. Deciding once at
    setup left the printer permanently without the swatches.
    """
    coordinator = _FakeCoordinator(None)  # first refresh failed / not in yet
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_setup_entry(hass, entry, async_add_entities)
    assert _slot_images(added) == []
    entry.async_on_unload.assert_called_once()  # still watching

    coordinator.publish(_machine_info(has_matl_station=True))

    assert len(_slot_images(added)) == IFS_SLOT_COUNT


@pytest.mark.unit
@pytest.mark.asyncio
async def test_slot_images_are_added_only_once():
    """Every later refresh must not add a second set of swatches."""
    coordinator = _FakeCoordinator(None)
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_setup_entry(hass, entry, async_add_entities)
    coordinator.publish(_machine_info(has_matl_station=True))
    coordinator.publish(_machine_info(has_matl_station=True))

    assert len(_slot_images(added)) == IFS_SLOT_COUNT


@pytest.mark.unit
@pytest.mark.asyncio
async def test_no_slot_images_without_a_station():
    """A printer that reports no station gets no swatches."""
    coordinator = _FakeCoordinator(_machine_info(has_matl_station=False))
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await image_setup_entry(hass, entry, async_add_entities)

    assert _slot_images(added) == []


@pytest.mark.unit
@pytest.mark.asyncio
async def test_gated_sensors_added_when_the_capability_reports_in_later():
    """Same rule for every availability_fn-gated sensor, not just the images."""
    coordinator = _FakeCoordinator(None)
    hass, entry, async_add_entities, added = _setup_args(coordinator)

    await sensor_setup_entry(hass, entry, async_add_entities)
    before = {getattr(e, "_attr_unique_id", "") for e in added}
    assert not any("ifs" in (uid or "") for uid in before)

    coordinator.publish(_machine_info(has_matl_station=True))

    after = {getattr(e, "_attr_unique_id", "") for e in added}
    assert any("ifs" in (uid or "") for uid in after - before)
