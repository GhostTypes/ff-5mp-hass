"""Serving and registering the FlashForge job card.

Named `card.py`, not `frontend.py`: a `frontend.py` module sitting beside the
`frontend/` directory that holds the JS resolves by import-machinery precedence
rather than by intent, and reads as a typo besides.

The card ships inside the integration rather than as a separate HACS frontend
repository, so installing the integration is the only step: the JS is served
from this package and registered as an extra frontend module at setup. Users
still add the card to a dashboard themselves - registration makes it *available*,
it does not place it anywhere.

Registration is global and idempotent per Home Assistant run: the static path and
the module URL are shared by every config entry, so the second printer must not
register them again (Home Assistant raises on a duplicate static path, and a
duplicate URL would load the card twice).
"""
from __future__ import annotations

import logging
from pathlib import Path

from homeassistant.components import persistent_notification
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store
from homeassistant.helpers.translation import async_get_translations

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

URL_BASE = f"/{DOMAIN}_frontend"
CARD_FILENAME = "ff-job-card.js"

_REGISTERED_KEY = f"{DOMAIN}_frontend_registered"

_STORE_KEY = f"{DOMAIN}.frontend"
_STORE_VERSION = 1
_NOTIFICATION_ID = f"{DOMAIN}_card_refresh"


async def async_register_frontend(hass: HomeAssistant, version: str) -> None:
    """Serve the card and register it with the frontend, once per run.

    ``version`` is appended to the module URL so an integration update is not
    served from the browser's cache; it is the manifest version, which every
    release bumps.
    """
    if hass.data.get(_REGISTERED_KEY):
        return
    hass.data[_REGISTERED_KEY] = True

    # Import here: `frontend` is an after_dependency, so it may be absent in a
    # stripped-down installation. The integration must still work without it -
    # only the card is lost.
    try:
        from homeassistant.components import frontend
    except ImportError:  # pragma: no cover - frontend is present in any real install
        _LOGGER.warning(
            "The frontend integration is unavailable, so the FlashForge job card "
            "will not be registered"
        )
        return

    # The whole directory, not just the JS: the card fetches its own copy from
    # `frontend/translations/<language>.json` at runtime, so those files have to
    # be reachable under the same URL base. Serving the directory also means a
    # new language is a new file and nothing else - no registration to update.
    #
    # Resolved from this module rather than from the config directory: the dev
    # sandbox reaches the integration through a symlink, and `custom_components/
    # flashforge` there is not a real path to the card.
    source = str(Path(__file__).parent / "frontend")
    await hass.http.async_register_static_paths(
        [
            StaticPathConfig(
                URL_BASE,
                source,
                # Cached by the browser; the ?v= query on each fetch is what
                # invalidates it, so a long cache here is safe and keeps
                # dashboards snappy.
                True,
            )
        ]
    )

    frontend.add_extra_js_url(hass, f"{URL_BASE}/{CARD_FILENAME}?v={version}")
    _LOGGER.debug("Registered the FlashForge job card (version %s)", version)

    await _async_notify_if_reload_needed(hass, version)


async def _async_notify_if_reload_needed(hass: HomeAssistant, version: str) -> None:
    """Tell already-open browser tabs to reload, once per card version.

    A browser loads the list of frontend modules with the page. Home Assistant
    has no way to add one to a page that is already open, so a tab that was
    loaded before this version existed - which is every tab, right after a HACS
    install and restart - keeps running without the card. The picker will not
    offer it and a dashboard using it renders "custom element doesn't exist",
    both of which read as a broken integration rather than a stale tab.

    A persistent notification is the one thing that *does* reach that tab: it
    arrives over the already-connected websocket and appears in the sidebar
    immediately, without a reload. So the fix is to reach the stale page and
    tell it what to do.

    Keyed on the card version, deliberately: the module URL carries that
    version, so it changing is exactly the condition under which an open tab is
    stale. An ordinary restart on an unchanged version needs no reload and
    stays silent - nagging on every restart is how a notification becomes
    something users learn to dismiss unread.
    """
    store: Store[dict[str, str]] = Store(hass, _STORE_VERSION, _STORE_KEY)
    try:
        data = await store.async_load() or {}
    except Exception:  # noqa: BLE001 - a broken store must not break setup
        _LOGGER.debug("Could not read the frontend store; skipping the notice")
        return

    if data.get("card_version") == version:
        return

    await store.async_save({"card_version": version})

    # Fall back to English if the translation is missing, so a language we do
    # not ship still gets an actionable message rather than a bare key.
    translations = await async_get_translations(
        hass, hass.config.language, "notifications", {DOMAIN}
    )
    prefix = f"component.{DOMAIN}.notifications.card_reload."
    title = translations.get(f"{prefix}title") or "FlashForge job card is ready"
    message = translations.get(f"{prefix}message") or (
        "The FlashForge Print Job card was just installed or updated. Reload this "
        "page (Ctrl+R, or Cmd+R on a Mac) to pick it up - until you do, the card "
        "will not appear in the card picker and dashboards already using it will "
        "show an error. This is only needed once per update."
    )

    persistent_notification.async_create(
        hass, message, title=title, notification_id=_NOTIFICATION_ID
    )
    _LOGGER.debug("Asked open browser tabs to reload for card version %s", version)
