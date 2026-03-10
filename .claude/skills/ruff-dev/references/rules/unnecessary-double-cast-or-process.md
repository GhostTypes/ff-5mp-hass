# [unnecessary-double-cast-or-process (C414)](#unnecessary-double-cast-or-process-c414)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-double-cast-or-process%27%20OR%20C414)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_double_cast_or_process.rs#L50)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `list()`, `reversed()`, `set()`, `sorted()`, and
`tuple()` call within `list()`, `set()`, `sorted()`, and `tuple()` calls.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to double-cast or double-process iterables by wrapping
the listed functions within an additional `list()`, `set()`, `sorted()`, or
`tuple()` call. Doing so is redundant and can be confusing for readers.

## [Example](#example)

```
list(tuple(iterable))
```

Use instead:

```
list(iterable)
```

This rule applies to a variety of functions, including `list()`, `reversed()`,
`set()`, `sorted()`, and `tuple()`. For example:

* Instead of `list(list(iterable))`, use `list(iterable)`.
* Instead of `list(tuple(iterable))`, use `list(iterable)`.
* Instead of `tuple(list(iterable))`, use `tuple(iterable)`.
* Instead of `tuple(tuple(iterable))`, use `tuple(iterable)`.
* Instead of `set(set(iterable))`, use `set(iterable)`.
* Instead of `set(list(iterable))`, use `set(iterable)`.
* Instead of `set(tuple(iterable))`, use `set(iterable)`.
* Instead of `set(sorted(iterable))`, use `set(iterable)`.
* Instead of `set(reversed(iterable))`, use `set(iterable)`.
* Instead of `sorted(list(iterable))`, use `sorted(iterable)`.
* Instead of `sorted(tuple(iterable))`, use `sorted(iterable)`.
* Instead of `sorted(sorted(iterable))`, use `sorted(iterable)`.
* Instead of `sorted(reversed(iterable))`, use `sorted(iterable)`.

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.