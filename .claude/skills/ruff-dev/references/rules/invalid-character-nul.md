# [invalid-character-nul (PLE2514)](#invalid-character-nul-ple2514)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-character-nul%27%20OR%20PLE2514)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_string_characters.rs#L136)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for strings that contain the raw control character `NUL` (0 byte).

## [Why is this bad?](#why-is-this-bad)

Control characters are displayed differently by different text editors and
terminals.

By using the `\0` sequence in lieu of the `NUL` control character, the
string will contain the same value, but will render visibly in all editors.

## [Example](#example)

```
x = ""
```

Use instead:

```
x = "\0"
```