# [isinstance-type-none (FURB168)](#isinstance-type-none-furb168)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27isinstance-type-none%27%20OR%20FURB168)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fisinstance_type_none.rs#L34)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `isinstance` that check if an object is of type `None`.

## [Why is this bad?](#why-is-this-bad)

There is only ever one instance of `None`, so it is more efficient and
readable to use the `is` operator to check if an object is `None`.

## [Example](#example)

```
isinstance(obj, type(None))
```

Use instead:

```
obj is None
```

## [Fix safety](#fix-safety)

The fix will be marked as unsafe if there are any comments within the call.

## [References](#references)

* [Python documentation: `isinstance`](https://docs.python.org/3/library/functions.html#isinstance)
* [Python documentation: `None`](https://docs.python.org/3/library/constants.html#None)
* [Python documentation: `type`](https://docs.python.org/3/library/functions.html#type)
* [Python documentation: Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)