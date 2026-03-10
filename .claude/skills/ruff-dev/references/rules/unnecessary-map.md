# [unnecessary-map (C417)](#unnecessary-map-c417)

Added in [v0.0.74](https://github.com/astral-sh/ruff/releases/tag/v0.0.74) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-map%27%20OR%20C417)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_map.rs#L46)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary `map()` calls with lambda functions.

## [Why is this bad?](#why-is-this-bad)

Using `map(func, iterable)` when `func` is a lambda is slower than
using a generator expression or a comprehension, as the latter approach
avoids the function call overhead, in addition to being more readable.

This rule also applies to `map()` calls within `list()`, `set()`, and
`dict()` calls. For example:

* Instead of `list(map(lambda num: num * 2, nums))`, use
  `[num * 2 for num in nums]`.
* Instead of `set(map(lambda num: num % 2 == 0, nums))`, use
  `{num % 2 == 0 for num in nums}`.
* Instead of `dict(map(lambda v: (v, v ** 2), values))`, use
  `{v: v ** 2 for v in values}`.

## [Example](#example)

```
map(lambda x: x + 1, iterable)
```

Use instead:

```
(x + 1 for x in iterable)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.