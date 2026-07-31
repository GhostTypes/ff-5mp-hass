"""Translation files stay in step with English.

Two independent sets of copy ship, and both are contributed to by people who
cannot run the integration against every model:

* ``translations/*.json`` - entity names, config-flow steps, error messages.
  Home Assistant loads these; a missing key renders as a raw translation key in
  the UI, and an extra key is dead weight that outlives the feature it named.
* ``frontend/translations/*.json`` - the job card's own copy, fetched by the
  card at runtime. English is the per-key fallback here, so a missing key
  degrades gracefully - but a mistyped ``{placeholder}`` does not: it renders
  literally, in the middle of a sentence, in the language that was supposed to
  be the polished one.

English is the reference in both cases. These tests are what makes accepting a
language PR safe without reading the language.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

COMPONENT = Path(__file__).parents[2] / "custom_components" / "flashforge"
HA_TRANSLATIONS = COMPONENT / "translations"
CARD_TRANSLATIONS = COMPONENT / "frontend" / "translations"

PLACEHOLDER = re.compile(r"\{(\w+)\}")


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _flatten(data: dict, prefix: str = "") -> dict[str, str]:
    """Nested translation dict to a flat {"a.b.c": value} mapping."""
    flat: dict[str, str] = {}
    for key, value in data.items():
        path = f"{prefix}{key}"
        if isinstance(value, dict):
            flat.update(_flatten(value, f"{path}."))
        else:
            flat[path] = value
    return flat


def _languages(directory: Path) -> list[Path]:
    """Every translation file except the English reference."""
    return sorted(p for p in directory.glob("*.json") if p.stem != "en")


def _ids(paths: list[Path]) -> list[str]:
    return [p.stem for p in paths]


HA_LANGUAGES = _languages(HA_TRANSLATIONS)
CARD_LANGUAGES = _languages(CARD_TRANSLATIONS)


def test_english_references_exist() -> None:
    """Both English files must exist - everything else is compared to them."""
    assert (HA_TRANSLATIONS / "en.json").is_file()
    assert (CARD_TRANSLATIONS / "en.json").is_file()


def test_strings_json_matches_english_translation() -> None:
    """`strings.json` and `translations/en.json` are the same key set.

    They are maintained by hand as two files with one meaning; the pair drifting
    is how a new entity ends up named in one place and not the other.
    """
    strings = set(_flatten(_load(COMPONENT / "strings.json")))
    english = set(_flatten(_load(HA_TRANSLATIONS / "en.json")))
    assert strings == english


@pytest.mark.parametrize("path", HA_LANGUAGES, ids=_ids(HA_LANGUAGES))
def test_ha_translation_key_sets_match_english(path: Path) -> None:
    """Home Assistant translations must be complete - it has no key fallback."""
    english = set(_flatten(_load(HA_TRANSLATIONS / "en.json")))
    translated = set(_flatten(_load(path)))

    assert not english - translated, f"{path.name} is missing keys"
    assert not translated - english, f"{path.name} has keys English does not"


@pytest.mark.parametrize("path", CARD_LANGUAGES, ids=_ids(CARD_LANGUAGES))
def test_card_translation_has_no_unknown_keys(path: Path) -> None:
    """A card translation may lag English, but may not invent keys.

    Missing keys fall back to English at runtime, so an incomplete translation
    is allowed on purpose. A key English does not have is either a typo - which
    silently falls back and looks like the translation was ignored - or a
    leftover from copy that has since been removed.
    """
    english = set(_load(CARD_TRANSLATIONS / "en.json"))
    translated = set(_load(path))
    assert not translated - english, f"{path.name} has keys English does not"


@pytest.mark.parametrize("path", CARD_LANGUAGES, ids=_ids(CARD_LANGUAGES))
def test_card_translation_placeholders_match(path: Path) -> None:
    """Every {placeholder} English uses must survive translation.

    The card substitutes by name and leaves unknown placeholders alone, so a
    dropped `{slot}` loses the slot number and a mistyped one renders as
    literal braces to the user.
    """
    english = _load(CARD_TRANSLATIONS / "en.json")
    translated = _load(path)

    for key, text in translated.items():
        if key not in english:
            continue  # reported by the unknown-key test
        expected = set(PLACEHOLDER.findall(english[key]))
        actual = set(PLACEHOLDER.findall(text))
        assert actual == expected, f"{path.name}: {key} placeholders differ"


@pytest.mark.parametrize("path", CARD_LANGUAGES, ids=_ids(CARD_LANGUAGES))
def test_card_plural_forms_are_complete(path: Path) -> None:
    """A translated plural needs both forms, or one count renders empty.

    `t.plural()` picks `_one` or `_other` and does not fall back across the
    pair, so translating only `tools_other` leaves the singular blank.
    """
    translated = _load(path)
    for key in translated:
        if key.endswith("_one"):
            assert f"{key[: -len('_one')]}_other" in translated, f"{path.name}: {key}"
        elif key.endswith("_other"):
            assert f"{key[: -len('_other')]}_one" in translated, f"{path.name}: {key}"


def test_card_strings_are_all_used() -> None:
    """Every key in the card's en.json is referenced by the card.

    Cheap protection against copy that outlives the UI it belonged to, and
    against a key renamed in the JS but not in the JSON - which renders empty
    rather than failing.
    """
    source = (COMPONENT / "frontend" / "ff-job-card.js").read_text(encoding="utf-8")

    used = set(re.findall(r"""_t(?:\.plural)?\(\s*["'](\w+)["']""", source))
    # Keys picked by a conditional inside the call, as in
    # `_t(this._starting ? "starting" : "start")`.
    for first, second in re.findall(r"""\?\s*["'](\w+)["']\s*:\s*["'](\w+)["']""", source):
        used.update({first, second})

    for key in _load(CARD_TRANSLATIONS / "en.json"):
        base = re.sub(r"_(one|other)$", "", key)
        assert base in used or key in used, f"{key} is not used by the card"
