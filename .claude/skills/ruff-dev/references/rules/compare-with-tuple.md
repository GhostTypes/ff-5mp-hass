# [compare-with-tuple (SIM109)](#compare-with-tuple-sim109)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27compare-with-tuple%27%20OR%20SIM109)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L96)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for boolean expressions that contain multiple equality comparisons
to the same value.

## [Why is this bad?](#why-is-this-bad)

To check if an object is equal to any one of multiple values, it's more
concise to use the `in` operator with a tuple of values.

## [Example](#example)

```
if foo == x or foo == y:
    ...
```

Use instead:

```
if foo in (x, y):
    ...
```

## [References](#references)

* [Python documentation: Membership test operations](https://docs.python.org/3/reference/expressions.html#membership-test-operations)