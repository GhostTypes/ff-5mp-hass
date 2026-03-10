# [unnecessary-subscript-reversal (C415)](#unnecessary-subscript-reversal-c415)

Added in [v0.0.64](https://github.com/astral-sh/ruff/releases/tag/v0.0.64) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-subscript-reversal%27%20OR%20C415)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_subscript_reversal.rs#L29)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

## [What it does](#what-it-does)

Checks for unnecessary subscript reversal of iterable.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to reverse the order of an iterable when passing it
into `reversed()`, `set()` or `sorted()` functions as they will change
the order of the elements again.

## [Example](#example)

```
sorted(iterable[::-1])
set(iterable[::-1])
reversed(iterable[::-1])
```

Use instead:

```
sorted(iterable)
set(iterable)
iterable
```