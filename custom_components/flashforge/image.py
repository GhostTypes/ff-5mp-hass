"""Image platform: g-code thumbnail + Material Station slot color swatches."""
from __future__ import annotations

from io import BytesIO
import logging
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

from homeassistant.components.image import ImageEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN
from .coordinator import FlashForgeDataUpdateCoordinator
from .util import build_device_info

_LOGGER = logging.getLogger(__name__)

IFS_SLOT_COUNT = 4
EMPTY_LABEL = "EMPTY"
EMPTY_COLOR = "#3A3A3A"
SWATCH_SIZE = 256

_FONT_CANDIDATES = (
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "C:/Windows/Fonts/segoeuib.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FlashForge image entities from a config entry."""
    coordinator: FlashForgeDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id][
        "coordinator"
    ]
    printer_name: str = hass.data[DOMAIN][entry.entry_id]["name"]

    async_add_entities(
        [FlashForgeThumbnailImage(hass, coordinator, printer_name, entry.entry_id)]
    )

    slots_added = False

    @callback
    def _async_add_slot_images() -> None:
        """Add the slot swatches once the printer reports a Material Station.

        Deciding this once at setup strands the entities permanently: platform
        setup can run before the station has reported in, and the first refresh
        may have failed outright. Keep watching instead.
        """
        nonlocal slots_added
        if slots_added or coordinator.data is None or not coordinator.data.has_matl_station:
            return
        slots_added = True
        async_add_entities(
            FlashForgeMaterialStationSlotImage(
                hass, coordinator, printer_name, entry.entry_id, slot_id
            )
            for slot_id in range(1, IFS_SLOT_COUNT + 1)
        )

    _async_add_slot_images()
    if not slots_added:
        entry.async_on_unload(coordinator.async_add_listener(_async_add_slot_images))


# --------------------------------------------------------------------------- #
# Swatch rendering helpers (pure, executor-friendly)
# --------------------------------------------------------------------------- #


def _hex_to_rgb(value: str) -> tuple[int, int, int] | None:
    """Convert '#RRGGBB' (or 'RRGGBB') to an (r, g, b) tuple."""
    if not value:
        return None
    cleaned = value.lstrip("#")
    if len(cleaned) != 6:
        return None
    try:
        return (int(cleaned[0:2], 16), int(cleaned[2:4], 16), int(cleaned[4:6], 16))
    except ValueError:
        return None


def _text_color_for(bg: tuple[int, int, int]) -> tuple[int, int, int]:
    """Pick black or white text based on perceived luminance of the background."""
    r, g, b = bg
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return (20, 20, 20) if luma > 140 else (245, 245, 245)


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in _FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    start_size: int,
    min_size: int = 24,
) -> tuple[ImageFont.FreeTypeFont | ImageFont.ImageFont, tuple[int, int, int, int]]:
    size = start_size
    while size > min_size:
        font = _load_font(size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            return font, bbox
        size -= 4
    font = _load_font(min_size)
    return font, draw.textbbox((0, 0), text, font=font)


def render_swatch_bytes(
    material: str, hex_color: str, *, size: int = SWATCH_SIZE
) -> bytes:
    """Render a PNG swatch (color + material label). Blocking — call via executor."""
    bg = _hex_to_rgb(hex_color) or _hex_to_rgb(EMPTY_COLOR) or (60, 60, 60)
    img = Image.new("RGB", (size, size), bg)
    draw = ImageDraw.Draw(img)

    border = (180, 180, 180) if sum(bg) > 600 else (40, 40, 40)
    draw.rectangle([(0, 0), (size - 1, size - 1)], outline=border, width=2)

    pad = int(size * 0.12)
    font, bbox = _fit_font(
        draw, material, size - 2 * pad, start_size=int(size * 0.36)
    )

    fg = _text_color_for(bg)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), material, fill=fg, font=font)

    buf = BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


# --------------------------------------------------------------------------- #
# Entities
# --------------------------------------------------------------------------- #


class FlashForgeThumbnailImage(
    CoordinatorEntity[FlashForgeDataUpdateCoordinator], ImageEntity
):
    """Image entity exposing the thumbnail of the currently printing g-code file."""

    _attr_has_entity_name = True
    _attr_translation_key = "current_file_thumbnail"
    _attr_content_type = "image/png"

    def __init__(
        self,
        hass: HomeAssistant,
        coordinator: FlashForgeDataUpdateCoordinator,
        printer_name: str,
        entry_id: str,
    ) -> None:
        CoordinatorEntity.__init__(self, coordinator)
        ImageEntity.__init__(self, hass)

        self._attr_unique_id = f"{entry_id}_thumbnail"
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

        self._cached_file: str | None = None
        self._cached_bytes: bytes | None = None

    def _current_file(self) -> str | None:
        if self.coordinator.data is None:
            return None
        name = getattr(self.coordinator.data, "print_file_name", None)
        return name or None

    @property
    def available(self) -> bool:
        return (
            self.coordinator.last_update_success
            and self._current_file() is not None
        )

    @property
    def extra_state_attributes(self) -> dict[str, str | None]:
        return {"file_name": self._current_file()}

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        current = self._current_file()
        if current is not None and self._attr_image_last_updated is None:
            self._cached_file = current
            self._attr_image_last_updated = dt_util.utcnow()

    def _handle_coordinator_update(self) -> None:
        current = self._current_file()
        if current != self._cached_file:
            self._cached_file = current
            self._cached_bytes = None
            self._attr_image_last_updated = dt_util.utcnow()
        super()._handle_coordinator_update()

    async def async_image(self) -> bytes | None:
        current = self._current_file()
        if current is None:
            return None

        if self._cached_bytes is not None and self._cached_file == current:
            return self._cached_bytes

        try:
            data = await self.coordinator.client.files.get_gcode_thumbnail(current)
        except Exception as err:  # noqa: BLE001
            _LOGGER.debug("Thumbnail fetch failed for %s: %s", current, err)
            return None

        if data:
            self._cached_file = current
            self._cached_bytes = data
        return data


class FlashForgeMaterialStationSlotImage(
    CoordinatorEntity[FlashForgeDataUpdateCoordinator], ImageEntity
):
    """Image entity rendering a Material Station slot as a labeled color swatch."""

    _attr_has_entity_name = True
    _attr_content_type = "image/png"

    def __init__(
        self,
        hass: HomeAssistant,
        coordinator: FlashForgeDataUpdateCoordinator,
        printer_name: str,
        entry_id: str,
        slot_id: int,
    ) -> None:
        CoordinatorEntity.__init__(self, coordinator)
        ImageEntity.__init__(self, hass)

        self._slot_id = slot_id
        self._attr_unique_id = f"{entry_id}_ifs_slot_{slot_id}"
        self._attr_translation_key = f"ifs_slot_{slot_id}"
        self._attr_device_info = build_device_info(coordinator, printer_name, entry_id)

        self._cached_key: tuple[str, str] | None = None
        self._cached_bytes: bytes | None = None

    def _slot(self) -> Any | None:
        data = self.coordinator.data
        if data is None or not data.has_matl_station:
            return None
        station = getattr(data, "matl_station_info", None)
        if station is None:
            return None
        for slot in getattr(station, "slot_infos", []) or []:
            if getattr(slot, "slot_id", None) == self._slot_id:
                return slot
        return None

    def _swatch_key(self) -> tuple[str, str]:
        """Return (label, hex_color) — what the swatch should depict."""
        slot = self._slot()
        if slot is None or not getattr(slot, "has_filament", False):
            return (EMPTY_LABEL, EMPTY_COLOR)
        material = (getattr(slot, "material_name", "") or "").strip().upper()
        color = (getattr(slot, "material_color", "") or "").strip()
        if _hex_to_rgb(color) is None:
            color = EMPTY_COLOR
        if not material:
            material = "?"
        return (material, color)

    @property
    def available(self) -> bool:
        if not self.coordinator.last_update_success:
            return False
        data = self.coordinator.data
        return bool(data and data.has_matl_station)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        slot = self._slot()
        if slot is None:
            return {"slot_id": self._slot_id, "has_filament": False}
        return {
            "slot_id": self._slot_id,
            "material": getattr(slot, "material_name", "") or None,
            "material_color": getattr(slot, "material_color", "") or None,
            "has_filament": bool(getattr(slot, "has_filament", False)),
        }

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        if self._attr_image_last_updated is None:
            self._cached_key = self._swatch_key()
            self._attr_image_last_updated = dt_util.utcnow()

    def _handle_coordinator_update(self) -> None:
        key = self._swatch_key()
        if key != self._cached_key:
            self._cached_key = key
            self._cached_bytes = None
            self._attr_image_last_updated = dt_util.utcnow()
        super()._handle_coordinator_update()

    async def async_image(self) -> bytes | None:
        key = self._swatch_key()
        if self._cached_bytes is not None and key == self._cached_key:
            return self._cached_bytes

        material, color = key
        data = await self.hass.async_add_executor_job(
            render_swatch_bytes, material, color
        )
        self._cached_key = key
        self._cached_bytes = data
        return data
