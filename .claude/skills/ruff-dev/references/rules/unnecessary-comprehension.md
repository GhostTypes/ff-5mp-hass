# [unnecessary-comprehension (C416)](#unnecessary-comprehension-c416)

Added in [v0.0.73](https://github.com/astral-sh/ruff/releases/tag/v0.0.73) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-comprehension%27%20OR%20C416)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_comprehension.rs#L59)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary dict, list, and set comprehension.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a dict/list/set comprehension to build a data structure if the
elements are unchanged. Wrap the iterable with `dict()`, `list()`, or `set()` instead.

## [Example](#example)

```
{a: b for a, b in iterable}
[x for x in iterable]
{x for x in iterable}
```

Use instead:

```
dict(iterable)
list(iterable)
set(iterable)
```

## [Known problems](#known-problems)

This rule may produce false positives for dictionary comprehensions that iterate over a mapping.
The dict constructor behaves differently depending on if it receives a sequence (e.g., a
list) or a mapping (e.g., a dict). When a comprehension iterates over the keys of a mapping,
replacing it with a `dict()` constructor call will give a different result.

For example:

```
>>> d1 = {(1, 2): 3, (4, 5): 6}
>>> {x: y for x, y in d1}  # Iterates over the keys of a mapping
{1: 2, 4: 5}
>>> dict(d1)               # Ruff's incorrect suggested fix
{(1, 2): 3, (4, 5): 6}
>>> dict(d1.keys())        # Correct fix
{1: 2, 4: 5}
```

When the comprehension iterates over a sequence, Ruff's suggested fix is correct. However, Ruff
cannot consistently infer if the iterable type is a sequence or a mapping and cannot suggest
the correct fix for mappings.

## [Fix safety](#fix-safety)

Due to the known problem with dictionary comprehensions, this fix is marked as unsafe.

Additionally, this fix may drop comments when rewriting the comprehension.