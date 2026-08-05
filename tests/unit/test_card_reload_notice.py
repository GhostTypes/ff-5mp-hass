"""The card's "reload this page" notice.

Home Assistant cannot add a frontend module to a page that is already open, so
after a HACS install and restart every open tab is running an index that
predates the card: the picker will not offer it and dashboards using it render
"custom element doesn't exist". A persistent notification is the one thing that
reaches those tabs, because it arrives over the websocket they are already
holding open.

What has to be true for that to be worth shipping:

* it fires when the card version changes - install or upgrade, the two moments
  a tab is genuinely stale;
* it stays silent on an ordinary restart, or the notification becomes noise
  users dismiss unread, which costs us the one moment it matters;
* it never takes setup down with it. The notice is a convenience; the card and
  the printer are not.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).parents[2]))

from tests.ha_mocks import Store, mock_homeassistant  # noqa: E402

mock_homeassistant()

from custom_components.flashforge import card as card_module  # noqa: E402


@pytest.fixture(autouse=True)
def _clean_state():
    """Each test starts with no stored version and a fresh notification mock."""
    Store.reset()
    card_module.persistent_notification.async_create.reset_mock()
    card_module.async_get_translations = AsyncMock(return_value={})
    yield
    Store.reset()


def _hass() -> MagicMock:
    hass = MagicMock()
    hass.data = {}
    hass.config.language = "en"
    hass.http.async_register_static_paths = AsyncMock()
    return hass


async def _register(hass: MagicMock, version: str) -> None:
    """Run a full registration pass, as one Home Assistant run would."""
    hass.data.pop(card_module._REGISTERED_KEY, None)
    await card_module.async_register_frontend(hass, version)


async def test_notifies_on_first_install() -> None:
    """Nothing stored means the card is new to this install - every tab is stale."""
    hass = _hass()
    await _register(hass, "1.4.0")

    create = card_module.persistent_notification.async_create
    assert create.call_count == 1
    assert create.call_args.kwargs["notification_id"] == card_module._NOTIFICATION_ID


async def test_silent_on_restart_with_unchanged_version() -> None:
    """The module URL did not change, so open tabs are fine. Say nothing."""
    hass = _hass()
    await _register(hass, "1.4.0")
    card_module.persistent_notification.async_create.reset_mock()

    await _register(hass, "1.4.0")

    assert card_module.persistent_notification.async_create.call_count == 0


async def test_notifies_again_on_upgrade() -> None:
    """A new version means a new module URL, so tabs are stale again."""
    hass = _hass()
    await _register(hass, "1.4.0")
    card_module.persistent_notification.async_create.reset_mock()

    await _register(hass, "1.4.1")

    assert card_module.persistent_notification.async_create.call_count == 1


async def test_uses_translated_text_when_available() -> None:
    """The notice follows the user's language like everything else."""
    hass = _hass()
    hass.config.language = "de"
    prefix = "component.flashforge.notifications.card_reload."
    card_module.async_get_translations = AsyncMock(
        return_value={f"{prefix}title": "Titel", f"{prefix}message": "Nachricht"}
    )

    await _register(hass, "1.4.0")

    create = card_module.persistent_notification.async_create
    assert create.call_args.args[1] == "Nachricht"
    assert create.call_args.kwargs["title"] == "Titel"


async def test_falls_back_to_english_for_untranslated_language() -> None:
    """A language we do not ship still gets an actionable message, not a key."""
    hass = _hass()
    hass.config.language = "fr"

    await _register(hass, "1.4.0")

    message = card_module.persistent_notification.async_create.call_args.args[1]
    assert "Reload this page" in message
    assert "component.flashforge" not in message


async def test_a_broken_store_does_not_break_setup() -> None:
    """The notice is a convenience; setup is not. Never trade one for the other."""
    hass = _hass()
    failing = MagicMock()
    failing.async_load = AsyncMock(side_effect=OSError("disk is unhappy"))
    original = card_module.Store
    card_module.Store = MagicMock(return_value=failing)
    try:
        await _register(hass, "1.4.0")
    finally:
        card_module.Store = original

    # Registration still completed; only the notice was skipped.
    hass.http.async_register_static_paths.assert_awaited()
    assert card_module.persistent_notification.async_create.call_count == 0
