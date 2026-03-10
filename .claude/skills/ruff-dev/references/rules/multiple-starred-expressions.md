# [multiple-starred-expressions (F622)](#multiple-starred-expressions-f622)

Added in [v0.0.32](https://github.com/astral-sh/ruff/releases/tag/v0.0.32) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-starred-expressions%27%20OR%20F622)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstarred_expressions.rs#L47)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for the use of multiple starred expressions in assignment statements.

## [Why is this bad?](#why-is-this-bad)

In assignment statements, starred expressions can be used to unpack iterables.
Including more than one starred expression on the left-hand-side of an
assignment will cause a `SyntaxError`, as it is unclear which expression
should receive the remaining values.

## [Example](#example)

```
*foo, *bar, baz = (1, 2, 3)
```

## [References](#references)

* [PEP 3132 – Extended Iterable Unpacking](https://peps.python.org/pep-3132/)