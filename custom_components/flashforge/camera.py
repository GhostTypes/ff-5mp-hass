"""Camera platform for FlashForge integration."""
from __future__ import annotations

import logging

from homeassistant.components.mjpeg.camera import MjpegCamera
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DEFAULT_CAMERA_PORT, DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge camera from a config entry."""
    ip_address: str = entry.data[CONF_IP_ADDRESS]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    camera = FlashForgeCamera(ip_address, printer_name, entry.entry_id)

    async_add_entities([camera])


class FlashForgeCamera(MjpegCamera):
    """Representation of a FlashForge camera."""

    _attr_has_entity_name = True

    def __init__(self, ip_address: str, printer_name: str, entry_id: str) -> None:
        """Initialize the camera."""
        self._ip_address = ip_address
        self._printer_name = printer_name
        self._entry_id = entry_id
        self._attr_unique_id = f"{entry_id}_camera"
        self._attr_name = "Camera"

        # FlashForge cameras typically use port 8080 with the ?action=stream endpoint
        mjpeg_url = f"http://{ip_address}:{DEFAULT_CAMERA_PORT}/?action=stream"

        super().__init__(
            name=self._attr_name,
            mjpeg_url=mjpeg_url,
            still_image_url=None,
        )

        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry_id)},
            "name": printer_name,
            "manufacturer": "FlashForge",
        }

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        # Camera availability is independent of coordinator
        # MJPEG camera will handle connection errors
        return True
