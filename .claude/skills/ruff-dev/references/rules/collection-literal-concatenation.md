# [collection-literal-concatenation (RUF005)](#collection-literal-concatenation-ruf005)

Added in [v0.0.227](https://github.com/astral-sh/ruff/releases/tag/v0.0.227) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27collection-literal-concatenation%27%20OR%20RUF005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fcollection_literal_concatenation.rs#L45)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of the `+` operator to concatenate collections.

## [Why is this bad?](#why-is-this-bad)

In Python, the `+` operator can be used to concatenate collections (e.g.,
`x + y` to concatenate the lists `x` and `y`).

However, collections can be concatenated more efficiently using the
unpacking operator (e.g., `[*x, *y]` to concatenate `x` and `y`).

Prefer the unpacking operator to concatenate collections, as it is more
readable and flexible. The `*` operator can unpack any iterable, whereas
`+` operates only on particular sequences which, in many cases, must be of
the same type.

## [Example](#example)

```
foo = [2, 3, 4]
bar = [1] + foo + [5, 6]
```

Use instead:

```
foo = [2, 3, 4]
bar = [1, *foo, 5, 6]
```

## [Fix safety](#fix-safety)

The fix is always marked as unsafe because the `+` operator uses the `__add__` magic method and
`*`-unpacking uses the `__iter__` magic method. Both of these could have custom
implementations, causing the fix to change program behaviour.

## [References](#references)

* [PEP 448 – Additional Unpacking Generalizations](https://peps.python.org/pep-0448/)
* [Python documentation: Sequence Types — `list`, `tuple`, `range`](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)