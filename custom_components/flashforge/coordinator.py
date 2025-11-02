"""DataUpdateCoordinator for FlashForge integration."""
from __future__ import annotations

from datetime import timedelta
import logging
from typing import Any

from flashforge import FlashForgeClient
from flashforge.models import FFMachineInfo, MachineState

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed

from .const import DOMAIN
from .util import async_close_flashforge_client

_LOGGER = logging.getLogger(__name__)


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

    async def _async_update_data(self) -> FFMachineInfo:
        """Fetch data from the printer."""
        try:
            # Get machine status using HTTP API
            machine_info = await self.client.info.get()

            if machine_info is None:
                raise UpdateFailed("Failed to retrieve printer status")

            return machine_info

        except Exception as err:
            _LOGGER.error("Error communicating with printer %s: %s", self.printer_name, err)
            raise UpdateFailed(f"Error communicating with printer: {err}") from err

    async def async_shutdown(self) -> None:
        """Shutdown the coordinator and cleanup resources."""
        await async_close_flashforge_client(self.client)
