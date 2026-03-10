# [unnecessary-generator-dict (C402)](#unnecessary-generator-dict-c402)

Added in [v0.0.61](https://github.com/astral-sh/ruff/releases/tag/v0.0.61) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-generator-dict%27%20OR%20C402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_generator_dict.rs#L34)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary generators that can be rewritten as dict
comprehensions.

## [Why is this bad?](#why-is-this-bad)

It is unnecessary to use `dict()` around a generator expression, since
there are equivalent comprehensions for these types. Using a
comprehension is clearer and more idiomatic.

## [Example](#example)

```
dict((x, f(x)) for x in foo)
```

Use instead:

```
{x: f(x) for x in foo}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.