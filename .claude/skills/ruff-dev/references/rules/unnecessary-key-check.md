# [unnecessary-key-check (RUF019)](#unnecessary-key-check-ruf019)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-key-check%27%20OR%20RUF019)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_key_check.rs#L31)

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary key checks prior to accessing a dictionary.

## [Why is this bad?](#why-is-this-bad)

When working with dictionaries, the `get` can be used to access a value
without having to check if the dictionary contains the relevant key,
returning `None` if the key is not present.

## [Example](#example)

```
if "key" in dct and dct["key"]:
    ...
```

Use instead:

```
if dct.get("key"):
    ...
```