# [star-arg-unpacking-after-keyword-arg (B026)](#star-arg-unpacking-after-keyword-arg-b026)

Added in [v0.0.109](https://github.com/astral-sh/ruff/releases/tag/v0.0.109) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27star-arg-unpacking-after-keyword-arg%27%20OR%20B026)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fstar_arg_unpacking_after_keyword_arg.rs#L48)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for function calls that use star-argument unpacking after providing a
keyword argument

## [Why is this bad?](#why-is-this-bad)

In Python, you can use star-argument unpacking to pass a list or tuple of
arguments to a function.

Providing a star-argument after a keyword argument can lead to confusing
behavior, and is only supported for backwards compatibility.

## [Example](#example)

```
def foo(x, y, z):
    return x, y, z


foo(1, 2, 3)  # (1, 2, 3)
foo(1, *[2, 3])  # (1, 2, 3)
# foo(x=1, *[2, 3])  # TypeError
# foo(y=2, *[1, 3])  # TypeError
foo(z=3, *[1, 2])  # (1, 2, 3)  # No error, but confusing!
```

Use instead:

```
def foo(x, y, z):
    return x, y, z


foo(1, 2, 3)  # (1, 2, 3)
foo(x=1, y=2, z=3)  # (1, 2, 3)
foo(*[1, 2, 3])  # (1, 2, 3)
foo(*[1, 2], 3)  # (1, 2, 3)
```

## [References](#references)

* [Python documentation: Calls](https://docs.python.org/3/reference/expressions.html#calls)
* [Disallow iterable argument unpacking after a keyword argument?](https://github.com/python/cpython/issues/82741)