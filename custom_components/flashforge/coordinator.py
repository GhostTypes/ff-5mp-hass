"""DataUpdateCoordinator for FlashForge integration."""
from __future__ import annotations

from datetime import timedelta
import logging

from flashforge import FlashForgeClient
from flashforge.models import FFGcodeFileEntry, FFMachineInfo

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, FILE_LIST_SCAN_INTERVAL, PRINTER_MODEL_NAMES
from .util import async_close_flashforge_client

_LOGGER = logging.getLogger(__name__)

UNKNOWN_MODEL = "Unknown"


class FlashForgeDataUpdateCoordinator(DataUpdateCoordinator[FFMachineInfo]):
    """Class to manage fetching FlashForge printer data."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: FlashForgeClient,
        name: str,
        scan_interval: int,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{name}",
            update_interval=timedelta(seconds=scan_interval),
        )
        self.client = client
        self.printer_name = name

    @property
    def device_model(self) -> str:
        """Return the human-readable model derived from the firmware-set PID."""
        if self.data is None:
            return UNKNOWN_MODEL
        pid = getattr(self.data, "pid", None)
        if pid is None:
            return UNKNOWN_MODEL
        return PRINTER_MODEL_NAMES.get(pid, UNKNOWN_MODEL)

    async def _async_update_data(self) -> FFMachineInfo:
        """Fetch data from the printer."""
        try:
            # Get machine status using HTTP API
            machine_info = await self.client.info.get()

            if machine_info is None:
                raise UpdateFailed("Failed to retrieve printer status")

            self.client.cache_details(machine_info)

            if not getattr(machine_info, "camera_stream_url", ""):
                detected_camera_stream = await self.client.detect_camera_stream()
                if detected_camera_stream:
                    machine_info.camera_stream_url = detected_camera_stream  # type: ignore[attr-defined]

            return machine_info

        except Exception as err:
            _LOGGER.error("Error communicating with printer %s: %s", self.printer_name, err)
            raise UpdateFailed(f"Error communicating with printer: {err}") from err

    async def async_shutdown(self) -> None:
        """Shutdown the coordinator and cleanup resources."""
        await async_close_flashforge_client(self.client)


class FlashForgeFileListCoordinator(DataUpdateCoordinator[list[FFGcodeFileEntry]]):
    """Class to manage fetching the printer's local g-code file list.

    Uses the HTTP ``/gcodeList`` endpoint, which reports the printer's most
    recent files (10 on current firmware) with their metadata. It is polled on a
    slower schedule than the machine state because the list only changes when a
    file is uploaded or removed.

    The client is owned by :class:`FlashForgeDataUpdateCoordinator`, so this
    coordinator never closes it.
    """

    def __init__(
        self,
        hass: HomeAssistant,
        client: FlashForgeClient,
        name: str,
    ) -> None:
        """Initialize the file list coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"{DOMAIN}_{name}_files",
            update_interval=timedelta(seconds=FILE_LIST_SCAN_INTERVAL),
        )
        self.client = client
        self.printer_name = name
        self.selected_file: str | None = None

    @property
    def file_names(self) -> list[str]:
        """Return the names of the files currently on the printer."""
        return [entry.gcode_file_name for entry in self.data or []]

    def entry_for(self, file_name: str) -> FFGcodeFileEntry | None:
        """Return the file list entry for a file name, if the printer reported one."""
        for entry in self.data or []:
            if entry.gcode_file_name == file_name:
                return entry
        return None

    async def _async_update_data(self) -> list[FFGcodeFileEntry]:
        """Fetch the local file list from the printer."""
        try:
            entries = await self.client.files.get_recent_file_list()
        except Exception as err:
            _LOGGER.error(
                "Error fetching file list from printer %s: %s", self.printer_name, err
            )
            raise UpdateFailed(f"Error fetching file list: {err}") from err

        return [entry for entry in entries or [] if entry.gcode_file_name]
