# [string-dot-format-mixing-automatic (F525)](#string-dot-format-mixing-automatic-f525)

Added in [v0.0.139](https://github.com/astral-sh/ruff/releases/tag/v0.0.139) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27string-dot-format-mixing-automatic%27%20OR%20F525)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstrings.rs#L551)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `str.format` calls that mix automatic and manual numbering.

## [Why is this bad?](#why-is-this-bad)

In `str.format` calls, mixing automatic and manual numbering will raise a
`ValueError` at runtime.

## [Example](#example)

```
"{0}, {}".format("Hello", "World")
```

Use instead:

```
"{0}, {1}".format("Hello", "World")
```

Or:

```
"{}, {}".format("Hello", "World")
```

## [References](#references)

* [Python documentation: `str.format`](https://docs.python.org/3/library/stdtypes.html#str.format)