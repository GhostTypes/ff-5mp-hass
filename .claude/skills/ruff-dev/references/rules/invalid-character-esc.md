# [invalid-character-esc (PLE2513)](#invalid-character-esc-ple2513)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-character-esc%27%20OR%20PLE2513)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_string_characters.rs#L100)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for strings that contain the raw control character `ESC`.

## [Why is this bad?](#why-is-this-bad)

Control characters are displayed differently by different text editors and
terminals.

By using the `\x1b` sequence in lieu of the `ESC` control character, the
string will contain the same value, but will render visibly in all editors.

## [Example](#example)

```
x = ""
```

Use instead:

```
x = "\x1b"
```