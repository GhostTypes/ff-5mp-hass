# [type-none-comparison (FURB169)](#type-none-comparison-furb169)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-none-comparison%27%20OR%20FURB169)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Ftype_none_comparison.rs#L34)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `type` that compare the type of an object to the type of `None`.

## [Why is this bad?](#why-is-this-bad)

There is only ever one instance of `None`, so it is more efficient and
readable to use the `is` operator to check if an object is `None`.

## [Example](#example)

```
type(obj) is type(None)
```

Use instead:

```
obj is None
```

## [Fix safety](#fix-safety)

If the fix might remove comments, it will be marked as unsafe.

## [References](#references)

* [Python documentation: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)
* [Python documentation: `None`](https://docs.python.org/3/library/constants.html#None)
* [Python documentation: `type`](https://docs.python.org/3/library/functions.html#type)
* [Python documentation: Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)