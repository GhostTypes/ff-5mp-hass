# [unpacked-list-comprehension (UP027)](#unpacked-list-comprehension-up027)

Removed (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unpacked-list-comprehension%27%20OR%20UP027)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Funpacked_list_comprehension.rs#L30)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

There's no [evidence](https://github.com/astral-sh/ruff/issues/12754) that generators are
meaningfully faster than list comprehensions when combined with unpacking.

## [What it does](#what-it-does)

Checks for list comprehensions that are immediately unpacked.

## [Why is this bad?](#why-is-this-bad)

There is no reason to use a list comprehension if the result is immediately
unpacked. Instead, use a generator expression, which avoids allocating
an intermediary list.

## [Example](#example)

```
a, b, c = [foo(x) for x in items]
```

Use instead:

```
a, b, c = (foo(x) for x in items)
```

## [References](#references)

* [Python documentation: Generator expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
* [Python documentation: List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)