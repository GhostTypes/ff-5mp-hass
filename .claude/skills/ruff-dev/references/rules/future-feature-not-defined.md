# [future-feature-not-defined (F407)](#future-feature-not-defined-f407)

Added in [v0.0.34](https://github.com/astral-sh/ruff/releases/tag/v0.0.34) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27future-feature-not-defined%27%20OR%20F407)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Ffuture_feature_not_defined.rs#L15)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `__future__` imports that are not defined in the current Python
version.

## [Why is this bad?](#why-is-this-bad)

Importing undefined or unsupported members from the `__future__` module is
a `SyntaxError`.

## [References](#references)

* [Python documentation: `__future__`](https://docs.python.org/3/library/__future__.html)