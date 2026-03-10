# [ruff-static-key-dict-comprehension (RUF011)](#ruff-static-key-dict-comprehension-ruf011)

Removed (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ruff-static-key-dict-comprehension%27%20OR%20RUF011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fstatic_key_dict_comprehension.rs#L30)

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule was implemented in `flake8-bugbear` and has been remapped to [B035](https://docs.astral.sh/ruff/rules/static-key-dict-comprehension/)

## [What it does](#what-it-does)

Checks for dictionary comprehensions that use a static key, like a string
literal or a variable defined outside the comprehension.

## [Why is this bad?](#why-is-this-bad)

Using a static key (like a string literal) in a dictionary comprehension
is usually a mistake, as it will result in a dictionary with only one key,
despite the comprehension iterating over multiple values.

## [Example](#example)

```
data = ["some", "Data"]
{"key": value.upper() for value in data}
```

Use instead:

```
data = ["some", "Data"]
{value: value.upper() for value in data}
```