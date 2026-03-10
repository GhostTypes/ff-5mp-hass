# [expr-and-not-expr (SIM220)](#expr-and-not-expr-sim220)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27expr-and-not-expr%27%20OR%20SIM220)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L130)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `and` expressions that include both an expression and its
negation.

## [Why is this bad?](#why-is-this-bad)

An `and` expression that includes both an expression and its negation will
always evaluate to `False`.

## [Example](#example)

```
x and not x
```

## [References](#references)

* [Python documentation: Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)