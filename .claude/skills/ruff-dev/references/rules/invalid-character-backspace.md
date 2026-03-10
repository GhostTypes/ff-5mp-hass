# [invalid-character-backspace (PLE2510)](#invalid-character-backspace-ple2510)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-character-backspace%27%20OR%20PLE2510)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_string_characters.rs#L28)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for strings that contain the control character `BS`.

## [Why is this bad?](#why-is-this-bad)

Control characters are displayed differently by different text editors and
terminals.

By using the `\b` sequence in lieu of the `BS` control character, the
string will contain the same value, but will render visibly in all editors.

## [Example](#example)

```
x = ""
```

Use instead:

```
x = "\b"
```