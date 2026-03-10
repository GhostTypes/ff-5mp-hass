# [bit-count (FURB161)](#bit-count-furb161)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bit-count%27%20OR%20FURB161)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fbit_count.rs#L41)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `bin(...).count("1")` to perform a population count.

## [Why is this bad?](#why-is-this-bad)

In Python 3.10, a `bit_count()` method was added to the `int` class,
which is more concise and efficient than converting to a binary
representation via `bin(...)`.

## [Example](#example)

```
x = bin(123).count("1")
y = bin(0b1111011).count("1")
```

Use instead:

```
x = (123).bit_count()
y = 0b1111011.bit_count()
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe unless the argument to `bin` can be inferred as
an instance of a type that implements the `__index__` and `bit_count` methods because this can
change the exception raised at runtime for an invalid argument.

## [Options](#options)

* [`target-version`](../../settings/#target-version)

## [References](#references)

* [Python documentation:`int.bit_count`](https://docs.python.org/3/library/stdtypes.html#int.bit_count)