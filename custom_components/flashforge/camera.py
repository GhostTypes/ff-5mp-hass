"""Camera platform for FlashForge integration."""
from __future__ import annotations

from homeassistant.components.mjpeg.camera import MjpegCamera
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge camera from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    camera = FlashForgeCamera(coordinator, printer_name, entry.entry_id)

    async_add_entities([camera])


class FlashForgeCamera(CoordinatorEntity[FlashForgeDataUpdateCoordinator], MjpegCamera):
    """Representation of a FlashForge camera."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: FlashForgeDataUpdateCoordinator,
        printer_name: str,
        entry_id: str,
    ) -> None:
        """Initialize the camera."""
        CoordinatorEntity.__init__(self, coordinator)
        self._attr_unique_id = f"{entry_id}_camera"
        self._attr_name = "Camera"

        MjpegCamera.__init__(
            self,
            name=self._attr_name,
            mjpeg_url=self._current_stream_url() or "http://127.0.0.1/",
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
        return (
            self.coordinator.last_update_success
            and self.coordinator.data is not None
            and bool(self._current_stream_url())
        )

    async def stream_source(self) -> str:
        """Return the current stream source reported by the printer."""
        stream_url = self._current_stream_url()
        if not stream_url:
            return ""
        self._mjpeg_url = stream_url
        return stream_url

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return a still image when a printer-reported stream URL is available."""
        if not self.available:
            return None
        self._sync_stream_url()
        return await super().async_camera_image(width, height)

    async def handle_async_mjpeg_stream(self, request):
        """Proxy the active MJPEG stream when the printer reports one."""
        if not self.available:
            return None
        self._sync_stream_url()
        return await super().handle_async_mjpeg_stream(request)

    def _current_stream_url(self) -> str:
        """Return the printer-reported OEM camera stream URL."""
        if self.coordinator.data is None:
            return ""
        return getattr(self.coordinator.data, "camera_stream_url", "") or ""

    def _sync_stream_url(self) -> None:
        """Keep the MJPEG camera base class pointed at the latest stream URL."""
        stream_url = self._current_stream_url()
        if stream_url:
            self._mjpeg_url = stream_url
