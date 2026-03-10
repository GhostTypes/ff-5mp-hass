# [native-literals (UP018)](#native-literals-up018)

Added in [v0.0.193](https://github.com/astral-sh/ruff/releases/tag/v0.0.193) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27native-literals%27%20OR%20UP018)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fnative_literals.rs#L130)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary calls to `str`, `bytes`, `int`, `float`, and `bool`.

## [Why is this bad?](#why-is-this-bad)

The mentioned constructors can be replaced with their respective literal
forms, which are more readable and idiomatic.

## [Example](#example)

```
str("foo")
```

Use instead:

```
"foo"
```

## [Fix safety](#fix-safety)

The fix is marked as unsafe if it might remove comments.

## [References](#references)

* [Python documentation: `str`](https://docs.python.org/3/library/stdtypes.html#str)
* [Python documentation: `bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)
* [Python documentation: `int`](https://docs.python.org/3/library/functions.html#int)
* [Python documentation: `float`](https://docs.python.org/3/library/functions.html#float)
* [Python documentation: `bool`](https://docs.python.org/3/library/functions.html#bool)