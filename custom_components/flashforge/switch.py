"""Switch platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge import FlashForgeClient
from flashforge.models import FFMachineInfo

from homeassistant.components.switch import SwitchEntity, SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


@dataclass
class FlashForgeSwitchEntityDescription(SwitchEntityDescription):
    """Describes FlashForge switch entity."""

    is_on_fn: Callable[[FFMachineInfo], bool] | None = None
    turn_on_fn: Callable[[FlashForgeClient], Any] | None = None
    turn_off_fn: Callable[[FlashForgeClient], Any] | None = None
    availability_fn: Callable[[FlashForgeClient], bool] | None = None


SWITCHES: tuple[FlashForgeSwitchEntityDescription, ...] = (
    FlashForgeSwitchEntityDescription(
        key="led",
        name="LED",
        icon="mdi:lightbulb",
        is_on_fn=lambda data: bool(getattr(data, "lights_on", False)),
        turn_on_fn=lambda client: client.control.set_led_on(),
        turn_off_fn=lambda client: client.control.set_led_off(),
        availability_fn=lambda client: client.led_control,
    ),
    FlashForgeSwitchEntityDescription(
        key="filtration",
        name="Filtration",
        icon="mdi:air-filter",
        is_on_fn=lambda data: bool(
            getattr(data, "external_fan_on", False) or getattr(data, "internal_fan_on", False)
        ),
        turn_on_fn=lambda client: client.control.set_external_filtration_on(),
        turn_off_fn=lambda client: client.control.set_filtration_off(),
        availability_fn=lambda client: client.filtration_control,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge switches from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    client: FlashForgeClient = hass.data[DOMAIN][entry.entry_id]["client"]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities = [
        FlashForgeSwitch(coordinator, client, description, printer_name, entry.entry_id)
        for description in SWITCHES
    ]

    async_add_entities(entities)


class FlashForgeSwitch(CoordinatorEntity[FlashForgeDataUpdateCoordinator], SwitchEntity):
    """Representation of a FlashForge switch."""

    entity_description: FlashForgeSwitchEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        client: FlashForgeClient,
        description: FlashForgeSwitchEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the switch."""
        super().__init__(coordinator)
        self.entity_description = description
        self._client = client
        self._attr_unique_id = f"{entry_id}_{description.key}"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": printer_name,
            "manufacturer": "FlashForge",
            "model": (
                coordinator.data.name
                if coordinator.data and getattr(coordinator.data, "name", None)
                else "Unknown"
            ),
        }

    @property
    def is_on(self) -> bool | None:
        """Return true if the switch is on."""
        if self.coordinator.data is None:
            return None

        if self.entity_description.is_on_fn:
            return self.entity_description.is_on_fn(self.coordinator.data)

        return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if not self.coordinator.last_update_success or self.coordinator.data is None:
            return False

        # Check if this feature is available on the printer
        if self.entity_description.availability_fn:
            return self.entity_description.availability_fn(self._client)

        return True

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the switch on."""
        if self.entity_description.turn_on_fn:
            try:
                await self.entity_description.turn_on_fn(self._client)
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error("Error turning on %s: %s", self.entity_description.name, err)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the switch off."""
        if self.entity_description.turn_off_fn:
            try:
                await self.entity_description.turn_off_fn(self._client)
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error(
                    "Error turning off %s: %s", self.entity_description.name, err
                )
