# [expr-or-not-expr (SIM221)](#expr-or-not-expr-sim221)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27expr-or-not-expr%27%20OR%20SIM221)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_bool_op.rs#L163)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `or` expressions that include both an expression and its
negation.

## [Why is this bad?](#why-is-this-bad)

An `or` expression that includes both an expression and its negation will
always evaluate to `True`.

## [Example](#example)

```
x or not x
```

## [References](#references)

* [Python documentation: Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)