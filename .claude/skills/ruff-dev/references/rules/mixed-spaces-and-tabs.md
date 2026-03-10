# [mixed-spaces-and-tabs (E101)](#mixed-spaces-and-tabs-e101)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mixed-spaces-and-tabs%27%20OR%20E101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fmixed_spaces_and_tabs.rs#L29)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for mixed tabs and spaces in indentation.

## [Why is this bad?](#why-is-this-bad)

Never mix tabs and spaces.

The most popular way of indenting Python is with spaces only. The
second-most popular way is with tabs only. Code indented with a
mixture of tabs and spaces should be converted to using spaces
exclusively.

## [Example](#example)

```
if a == 0:\n        a = 1\n\tb = 1
```

Use instead:

```
if a == 0:\n    a = 1\n    b = 1
```