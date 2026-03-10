# [double-negation (SIM208)](#double-negation-sim208)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27double-negation%27%20OR%20SIM208)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_unary_op.rs#L116)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for double negations (i.e., multiple `not` operators).

## [Why is this bad?](#why-is-this-bad)

A double negation is redundant and less readable than omitting the `not`
operators entirely.

## [Example](#example)

```
not (not a)
```

Use instead:

```
a
```

## [References](#references)

* [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)