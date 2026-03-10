# [if-expr-with-twisted-arms (SIM212)](#if-expr-with-twisted-arms-sim212)

Added in [v0.0.214](https://github.com/astral-sh/ruff/releases/tag/v0.0.214) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-expr-with-twisted-arms%27%20OR%20SIM212)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_ifexp.rs#L122)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `if` expressions that check against a negated condition.

## [Why is this bad?](#why-is-this-bad)

`if` expressions that check against a negated condition are more difficult
to read than `if` expressions that check against the condition directly.

## [Example](#example)

```
b if not a else a
```

Use instead:

```
a if a else b
```

## [References](#references)

* [Python documentation: Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)