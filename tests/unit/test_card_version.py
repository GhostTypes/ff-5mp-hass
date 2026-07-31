"""The card's version constant tracks the manifest.

Two different values do the browser cache-busting for one card:

* `card.py` appends the **manifest** version to the module URL, which is what
  makes a released update reach a browser holding the previous file.
* `ff-job-card.js` appends its own `CARD_VERSION` to the translation files it
  fetches at runtime.

Let those drift and a release ships new JavaScript against translation URLs the
browser already has cached - the card updates, its copy does not, and the
symptom is untranslated or outdated strings that look like a translation bug
and are not. Home Assistant's service worker caches by URL, so the only thing
standing between a user and stale copy is the query string changing.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

COMPONENT = Path(__file__).parents[2] / "custom_components" / "flashforge"


def test_card_version_matches_manifest() -> None:
    manifest = json.loads((COMPONENT / "manifest.json").read_text(encoding="utf-8"))
    source = (COMPONENT / "frontend" / "ff-job-card.js").read_text(encoding="utf-8")

    match = re.search(r"""const CARD_VERSION = ["']([^"']+)["']""", source)
    assert match, "CARD_VERSION is not declared in ff-job-card.js"

    assert match.group(1) == manifest["version"], (
        "CARD_VERSION and manifest.json version disagree; bump both or the "
        "card's translations will be served from a stale browser cache"
    )


def test_translations_are_cache_busted() -> None:
    """The translation fetch must carry the version, or it is cached forever.

    `card.py` serves `frontend/` with long-lived cache headers, which is only
    safe because every URL under it carries a version that a release changes.
    """
    source = (COMPONENT / "frontend" / "ff-job-card.js").read_text(encoding="utf-8")
    assert "?v=${CARD_VERSION}" in source
