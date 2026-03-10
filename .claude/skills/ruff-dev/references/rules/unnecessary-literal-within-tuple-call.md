# [unnecessary-literal-within-tuple-call (C409)](#unnecessary-literal-within-tuple-call-c409)

Added in [v0.0.66](https://github.com/astral-sh/ruff/releases/tag/v0.0.66) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-literal-within-tuple-call%27%20OR%20C409)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_literal_within_tuple_call.rs#L50)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `tuple` calls that take unnecessary list or tuple literals as
arguments. In [preview](https://docs.astral.sh/ruff/preview/), this also includes unnecessary list comprehensions
within tuple calls.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a list or tuple literal within a `tuple()` call,
since there is a literal syntax for these types.

If a list literal was passed, then it should be rewritten as a `tuple`
literal. Otherwise, if a tuple literal was passed, then the outer call
to `tuple()` should be removed.

In [preview](https://docs.astral.sh/ruff/preview/), this rule also checks for list comprehensions within `tuple()`
calls. If a list comprehension is found, it should be rewritten as a
generator expression.

## [Example](#example)

```
tuple([1, 2])
tuple((1, 2))
tuple([x for x in range(10)])
```

Use instead:

```
(1, 2)
(1, 2)
tuple(x for x in range(10))
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.