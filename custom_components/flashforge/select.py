"""Select platform for FlashForge integration."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging
from typing import Any

from flashforge import FlashForgeClient
from flashforge.models import FFGcodeFileEntry, FFMachineInfo
import voluptuous as vol

from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import config_validation as cv, entity_platform
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    ATTR_FILE_NAME,
    ATTR_LEVELING_BEFORE_PRINT,
    CONF_LEVELING_BEFORE_PRINT,
    DEFAULT_LEVELING_BEFORE_PRINT,
    DOMAIN,
    SERVICE_PRINT_FILE,
)
from .coordinator import FlashForgeDataUpdateCoordinator, FlashForgeFileListCoordinator
from .print_job import async_start_local_print
from .util import build_device_info

_LOGGER = logging.getLogger(__name__)

PRINT_FILE_SCHEMA = {
    vol.Optional(ATTR_FILE_NAME): cv.string,
    vol.Optional(ATTR_LEVELING_BEFORE_PRINT): cv.boolean,
}


def file_attributes(entry: FFGcodeFileEntry) -> dict[str, Any]:
    """Describe one file, reporting only what the printer actually told us.

    ``/gcodeList`` returns per-file metadata (``gcodeListDetail``) on the AD5X,
    but plain file names on the Creator 5 series. Absent values are left out
    rather than reported as 0 / False, so a multi-material file on a printer
    that reports no metadata is not mistaken for a single-material one.
    """
    attributes: dict[str, Any] = {"name": entry.gcode_file_name}
    if entry.printing_time:
        attributes["printing_time"] = entry.printing_time
    if entry.total_filament_weight is not None:
        attributes["filament_weight"] = entry.total_filament_weight
    if entry.gcode_tool_cnt is not None:
        attributes["tool_count"] = entry.gcode_tool_cnt
    if entry.use_matl_station is not None:
        attributes["uses_material_station"] = entry.use_matl_station
    return attributes


@dataclass
class FlashForgeSelectEntityDescription(SelectEntityDescription):
    """Describes FlashForge select entity."""

    current_fn: Callable[[FFMachineInfo], str | None] | None = None
    select_fn: Callable[[FlashForgeClient, str], Any] | None = None
    availability_fn: Callable[[FFMachineInfo], bool] | None = None


SELECTS: tuple[FlashForgeSelectEntityDescription, ...] = (
    FlashForgeSelectEntityDescription(
        key="filtration_mode",
        translation_key="filtration_mode",
        icon="mdi:air-filter",
        options=["Off", "Internal", "External"],
        current_fn=lambda data: (
            "External" if getattr(data, "external_fan_on", False)
            else "Internal" if getattr(data, "internal_fan_on", False)
            else "Off"
        ),
        select_fn=lambda client, option: (
            client.control.set_external_filtration_on() if option == "External"
            else client.control.set_internal_filtration_on() if option == "Internal"
            else client.control.set_filtration_off()
        ),
        availability_fn=lambda data: bool(
            getattr(data, "is_pro", False) or getattr(data, "is_creator5_pro", False)
        ),
    ),
)


async def _async_print_file_service(entity: Entity, call: ServiceCall) -> None:
    """Handle the ``flashforge.print_file`` entity service."""
    if not isinstance(entity, FlashForgeFileSelect):
        raise ServiceValidationError(
            f"{SERVICE_PRINT_FILE} must target a FlashForge print file entity, "
            f"got {entity.entity_id}"
        )

    await entity.async_print_file(
        call.data.get(ATTR_FILE_NAME),
        call.data.get(ATTR_LEVELING_BEFORE_PRINT),
    )


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge select entities from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    file_coordinator: FlashForgeFileListCoordinator = hass.data[DOMAIN][entry.entry_id][
        "file_coordinator"
    ]
    client: FlashForgeClient = hass.data[DOMAIN][entry.entry_id]["client"]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    entities: list[SelectEntity] = [
        FlashForgeSelect(coordinator, client, description, printer_name, entry.entry_id)
        for description in SELECTS
    ]
    entities.append(
        FlashForgeFileSelect(
            coordinator, file_coordinator, client, entry, printer_name
        )
    )

    async_add_entities(entities)

    entity_platform.async_get_current_platform().async_register_entity_service(
        SERVICE_PRINT_FILE, PRINT_FILE_SCHEMA, _async_print_file_service
    )


class FlashForgeSelect(CoordinatorEntity[FlashForgeDataUpdateCoordinator], SelectEntity):
    """Representation of a FlashForge select entity."""

    entity_description: FlashForgeSelectEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        client: FlashForgeClient,
        description: FlashForgeSelectEntityDescription,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the select entity."""
        super().__init__(coordinator)
        self.entity_description = description
        self._client = client
        self._attr_unique_id = f"{entry_id}_{description.key}"
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

    @property
    def current_option(self) -> str | None:
        """Return the current selected option."""
        if self.coordinator.data is None:
            return None

        if self.entity_description.current_fn:
            return self.entity_description.current_fn(self.coordinator.data)

        return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if not self.coordinator.last_update_success or self.coordinator.data is None:
            return False

        # Check if this feature is available on the printer
        if self.entity_description.availability_fn:
            return self.entity_description.availability_fn(self.coordinator.data)

        return True

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        if self.entity_description.select_fn:
            try:
                await self.entity_description.select_fn(self._client, option)
                await self.coordinator.async_request_refresh()
            except Exception as err:
                _LOGGER.error(
                    "Error selecting option %s for %s: %s",
                    option,
                    self.entity_description.name,
                    err,
                )


class FlashForgeFileSelect(
    CoordinatorEntity[FlashForgeFileListCoordinator], SelectEntity
):
    """Lists the files stored on the printer and holds the one picked for printing.

    Selecting an option only records the choice; the print is started by the
    "Print Selected File" button or the ``flashforge.print_file`` service.
    """

    _attr_has_entity_name = True
    _attr_translation_key = "print_file"
    _attr_icon = "mdi:file-document-multiple-outline"

    def __init__(
        self,
        machine_coordinator: FlashForgeDataUpdateCoordinator,
        coordinator: FlashForgeFileListCoordinator,
        client: FlashForgeClient,
        entry: ConfigEntry,
        printer_name: str,
    ) -> None:
        """Initialize the print file select entity."""
        super().__init__(coordinator)
        self._machine_coordinator = machine_coordinator
        self._client = client
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_print_file"
        self._attr_device_info = build_device_info(
            machine_coordinator, printer_name, entry.entry_id
        )

    @property
    def options(self) -> list[str]:
        """Return the files currently stored on the printer."""
        return self.coordinator.file_names

    @property
    def current_option(self) -> str | None:
        """Return the file picked for printing, if it is still on the printer."""
        selected = self.coordinator.selected_file
        if selected is None or selected not in self.options:
            return None
        return selected

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the metadata the printer reports for each file."""
        return {
            "files": [file_attributes(entry) for entry in self.coordinator.data or []]
        }

    async def async_select_option(self, option: str) -> None:
        """Record the file to print."""
        if option not in self.options:
            raise ServiceValidationError(f"'{option}' is not a file on the printer")

        self.coordinator.selected_file = option
        # Only this entity's state changed. Notifying the coordinator's listeners
        # would also rewrite the stateless print button's state, which the
        # logbook reports as a button press that never happened.
        self.async_write_ha_state()

    async def async_print_file(
        self,
        file_name: str | None = None,
        leveling_before_print: bool | None = None,
    ) -> None:
        """Start printing a file that is stored on the printer.

        Defaults to the currently selected file and to the bed-leveling setting
        from the integration options.
        """
        target = (file_name or self.current_option or "").strip()
        if not target:
            raise ServiceValidationError(
                "No file to print: select a file first or pass a file name"
            )

        if leveling_before_print is None:
            leveling_before_print = self._entry.options.get(
                CONF_LEVELING_BEFORE_PRINT, DEFAULT_LEVELING_BEFORE_PRINT
            )

        await async_start_local_print(
            self._client,
            target,
            leveling_before_print=bool(leveling_before_print),
            file_entry=self.coordinator.entry_for(target),
            machine_info=self._machine_coordinator.data,
        )

        await self._machine_coordinator.async_request_refresh()
