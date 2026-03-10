# [type-of-primitive (UP003)](#type-of-primitive-up003)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-of-primitive%27%20OR%20UP003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Ftype_of_primitive.rs#L32)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `type` that take a primitive as an argument.

## [Why is this bad?](#why-is-this-bad)

`type()` returns the type of a given object. A type of a primitive can
always be known in advance and accessed directly, which is more concise
and explicit than using `type()`.

## [Example](#example)

```
type(1)
```

Use instead:

```
int
```

## [References](#references)

* [Python documentation: `type()`](https://docs.python.org/3/library/functions.html#type)
* [Python documentation: Built-in types](https://docs.python.org/3/library/stdtypes.html)