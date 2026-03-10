# [static-key-dict-comprehension (B035)](#static-key-dict-comprehension-b035)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27static-key-dict-comprehension%27%20OR%20B035)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fstatic_key_dict_comprehension.rs#L33)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

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