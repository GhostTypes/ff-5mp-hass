# [os-error-alias (UP024)](#os-error-alias-up024)

Added in [v0.0.206](https://github.com/astral-sh/ruff/releases/tag/v0.0.206) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-error-alias%27%20OR%20UP024)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fos_error_alias.rs#L37)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of exceptions that alias `OSError`.

## [Why is this bad?](#why-is-this-bad)

`OSError` is the builtin error type used for exceptions that relate to the
operating system.

In Python 3.3, a variety of other exceptions, like `WindowsError` were
aliased to `OSError`. These aliases remain in place for compatibility with
older versions of Python, but may be removed in future versions.

Prefer using `OSError` directly, as it is more idiomatic and future-proof.

## [Example](#example)

```
raise IOError
```

Use instead:

```
raise OSError
```

## [References](#references)

* [Python documentation: `OSError`](https://docs.python.org/3/library/exceptions.html#OSError)