# [negate-not-equal-op (SIM202)](#negate-not-equal-op-sim202)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27negate-not-equal-op%27%20OR%20SIM202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_unary_op.rs#L78)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for negated `!=` operators.

## [Why is this bad?](#why-is-this-bad)

Negated `!=` operators are less readable than `==` operators, as they avoid a
double negation.

## [Example](#example)

```
not a != b
```

Use instead:

```
a == b
```

## [Fix safety](#fix-safety)

The fix is marked as unsafe, as it might change the behaviour
if `a` and/or `b` overrides `__ne__`/`__eq__`
in such a manner that they don't return booleans.

## [References](#references)

* [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)