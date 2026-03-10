# [type-check-without-type-error (TRY004)](#type-check-without-type-error-try004)

Added in [v0.0.230](https://github.com/astral-sh/ruff/releases/tag/v0.0.230) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-check-without-type-error%27%20OR%20TRY004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Ftype_check_without_type_error.rs#L38)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

## [What it does](#what-it-does)

Checks for type checks that do not raise `TypeError`.

## [Why is this bad?](#why-is-this-bad)

The Python documentation states that `TypeError` should be raised upon
encountering an inappropriate type.

## [Example](#example)

```
def foo(n: int):
    if isinstance(n, int):
        pass
    else:
        raise ValueError("n must be an integer")
```

Use instead:

```
def foo(n: int):
    if isinstance(n, int):
        pass
    else:
        raise TypeError("n must be an integer")
```

## [References](#references)

* [Python documentation: `TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError)