# [string-dot-format-invalid-format (F521)](#string-dot-format-invalid-format-f521)

Added in [v0.0.138](https://github.com/astral-sh/ruff/releases/tag/v0.0.138) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-dot-format-invalid-format%27%20OR%20F521)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L373)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `str.format` calls with invalid format strings.

## [Why is this bad?](#why-is-this-bad)

Invalid format strings will raise a `ValueError`.

## [Example](#example)

```
"{".format(foo)
```

Use instead:

```
"{}".format(foo)
```

## [References](#references)

* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)