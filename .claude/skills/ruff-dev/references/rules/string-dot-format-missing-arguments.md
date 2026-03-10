# [string-dot-format-missing-arguments (F524)](#string-dot-format-missing-arguments-f524)

Added in [v0.0.139](https://github.com/astral-sh/ruff/releases/tag/v0.0.139) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-dot-format-missing-arguments%27%20OR%20F524)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L512)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `str.format` calls with placeholders that are missing arguments.

## [Why is this bad?](#why-is-this-bad)

In `str.format` calls, omitting arguments for placeholders will raise a
`KeyError` at runtime.

## [Example](#example)

```
"{greeting}, {name}".format(name="World")
```

Use instead:

```
"{greeting}, {name}".format(greeting="Hello", name="World")
```

## [References](#references)

* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)