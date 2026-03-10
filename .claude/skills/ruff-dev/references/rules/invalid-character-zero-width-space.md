# [invalid-character-zero-width-space (PLE2515)](#invalid-character-zero-width-space-ple2515)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-character-zero-width-space%27%20OR%20PLE2515)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_string_characters.rs#L171)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for strings that contain the zero width space character.

## [Why is this bad?](#why-is-this-bad)

This character is rendered invisibly in some text editors and terminals.

By using the `\u200B` sequence, the string will contain the same value,
but will render visibly in all editors.

## [Example](#example)

```
x = "Dear Sir/Madam"
```

Use instead:

```
x = "Dear Sir\u200b/\u200bMadam"  # zero width space
```