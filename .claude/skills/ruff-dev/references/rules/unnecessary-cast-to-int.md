# [unnecessary-cast-to-int (RUF046)](#unnecessary-cast-to-int-ruf046)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-cast-to-int%27%20OR%20RUF046)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_cast_to_int.rs#L47)

Fix is always available.

## [What it does](#what-it-does)

Checks for `int` conversions of values that are already integers.

## [Why is this bad?](#why-is-this-bad)

Such a conversion is unnecessary.

## [Known problems](#known-problems)

This rule may produce false positives for `round`, `math.ceil`, `math.floor`,
and `math.trunc` calls when values override the `__round__`, `__ceil__`, `__floor__`,
or `__trunc__` operators such that they don't return an integer.

## [Example](#example)

```
int(len([]))
int(round(foo, None))
```

Use instead:

```
len([])
round(foo)
```

## [Fix safety](#fix-safety)

The fix for `round`, `math.ceil`, `math.floor`, and `math.truncate` is unsafe
because removing the `int` conversion can change the semantics for values
overriding the `__round__`, `__ceil__`, `__floor__`, or `__trunc__` dunder methods
such that they don't return an integer.