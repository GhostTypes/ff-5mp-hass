# [expressions-in-star-assignment (F621)](#expressions-in-star-assignment-f621)

Added in [v0.0.32](https://github.com/astral-sh/ruff/releases/tag/v0.0.32) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27expressions-in-star-assignment%27%20OR%20F621)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fstarred_expressions.rs#L20)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for the use of too many expressions in starred assignment statements.

## [Why is this bad?](#why-is-this-bad)

In assignment statements, starred expressions can be used to unpack iterables.

In Python 3, no more than `1 << 8` assignments are allowed before a starred
expression, and no more than `1 << 24` expressions are allowed after a starred
expression.

## [References](#references)

* [PEP 3132 – Extended Iterable Unpacking](https://peps.python.org/pep-3132/)