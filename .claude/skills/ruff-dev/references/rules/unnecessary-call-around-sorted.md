# [unnecessary-call-around-sorted (C413)](#unnecessary-call-around-sorted-c413)

Added in [v0.0.73](https://github.com/astral-sh/ruff/releases/tag/v0.0.73) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-call-around-sorted%27%20OR%20C413)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_call_around_sorted.rs#L44)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `list()` or `reversed()` calls around `sorted()`
calls.

## [Why is this bad?](#why-is-this-bad)

It is unnecessary to use `list()` around `sorted()`, as the latter already
returns a list.

It is also unnecessary to use `reversed()` around `sorted()`, as the latter
has a `reverse` argument that can be used in lieu of an additional
`reversed()` call.

In both cases, it's clearer and more efficient to avoid the redundant call.

## [Example](#example)

```
reversed(sorted(iterable))
```

Use instead:

```
sorted(iterable, reverse=True)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for `reversed()` cases, as `reversed()`
and `reverse=True` will yield different results in the event of custom sort
keys or equality functions. Specifically, `reversed()` will reverse the order
of the collection, while `sorted()` with `reverse=True` will perform a stable
reverse sort, which will preserve the order of elements that compare as
equal.

The fix is marked as safe for `list()` cases, as removing `list()` around
`sorted()` does not change the behavior.