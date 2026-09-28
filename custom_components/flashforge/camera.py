"""Camera platform for FlashForge integration."""

from __future__ import annotations

from aiohttp import web
from homeassistant.components.camera import Camera, async_get_still_stream
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event, HomeAssistant, callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .camera_stream import SharedCameraStream
from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator
from .util import build_device_info


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


class FlashForgeCamera(CoordinatorEntity[FlashForgeDataUpdateCoordinator], Camera):
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
        Camera.__init__(self)
        self._attr_unique_id = f"{entry_id}_camera"
        self._attr_translation_key = "camera"

        self._shared_stream: SharedCameraStream | None = None

        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

    async def async_added_to_hass(self) -> None:
        """Release the upstream before HA cancels background tasks at shutdown."""
        await super().async_added_to_hass()
        self.async_on_remove(
            self.hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, self._async_stop)
        )

    async def _async_stop(self, event: Event) -> None:
        if self._shared_stream is not None:
            await self._shared_stream.close()

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
        return self._current_stream_url()

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return a still image when a printer-reported stream URL is available."""
        if not self.available:
            return None
        async with self._get_stream().subscribe() as stream:
            frame = await stream.frame()
            return frame[1] if frame else None

    async def handle_async_mjpeg_stream(
        self, request: web.Request
    ) -> web.StreamResponse | None:
        """Share one printer connection across all live previews and snapshots."""
        if not self.available:
            return None
        async with self._get_stream().subscribe() as stream:
            sequence = -1

            async def next_image() -> bytes | None:
                nonlocal sequence
                frame = await stream.frame(sequence)
                if frame is None:
                    return None
                sequence, image = frame
                return image

            return await async_get_still_stream(
                request, next_image, self.content_type, 0
            )

    @callback
    def _handle_coordinator_update(self) -> None:
        """Drop the old source immediately on camera off, offline, or URL change."""
        if self._shared_stream is not None:
            self._shared_stream.set_url(
                self._current_stream_url() if self.available else None
            )
        super()._handle_coordinator_update()

    async def async_will_remove_from_hass(self) -> None:
        """Stop the background reader when the integration unloads."""
        if self._shared_stream is not None:
            await self._shared_stream.close()
        await super().async_will_remove_from_hass()

    def _get_stream(self) -> SharedCameraStream:
        if self._shared_stream is None:
            self._shared_stream = SharedCameraStream(
                async_get_clientsession(self.hass),
                lambda coro: self.hass.async_create_background_task(
                    coro, "flashforge camera"
                ),
            )
        self._shared_stream.set_url(
            self._current_stream_url() if self.available else None
        )
        return self._shared_stream

    def _current_stream_url(self) -> str:
        """Return the printer-reported OEM camera stream URL."""
        if self.coordinator.data is None:
            return ""
        return getattr(self.coordinator.data, "camera_stream_url", "") or ""
