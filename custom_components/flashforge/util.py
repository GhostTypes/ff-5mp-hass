"""Utility helpers for the FlashForge integration."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flashforge import FlashForgeClient


async def async_close_flashforge_client(client: "FlashForgeClient") -> None:
    """Close any HTTP resources held by the FlashForge client without touching TCP."""
    session = getattr(client, "_http_session", None)
    if session and not session.closed:
        await session.close()
