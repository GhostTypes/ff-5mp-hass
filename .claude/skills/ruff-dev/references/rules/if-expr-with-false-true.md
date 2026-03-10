# [if-expr-with-false-true (SIM211)](#if-expr-with-false-true-sim211)

Added in [v0.0.214](https://github.com/astral-sh/ruff/releases/tag/v0.0.214) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-expr-with-false-true%27%20OR%20SIM211)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_ifexp.rs#L88)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `if` expressions that can be replaced by negating a given
condition.

## [Why is this bad?](#why-is-this-bad)

`if` expressions that evaluate to `False` for a truthy condition and `True`
for a falsey condition can be replaced with `not` operators, which are more
concise and readable.

## [Example](#example)

```
False if a else True
```

Use instead:

```
not a
```

## [References](#references)

* [Python documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)