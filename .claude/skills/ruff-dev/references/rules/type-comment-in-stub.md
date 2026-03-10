# [type-comment-in-stub (PYI033)](#type-comment-in-stub-pyi033)

Added in [v0.0.254](https://github.com/astral-sh/ruff/releases/tag/v0.0.254) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27type-comment-in-stub%27%20OR%20PYI033)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Ftype_comment_in_stub.rs#L30)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for the use of type comments (e.g., `x = 1 # type: int`) in stub
files.

## [Why is this bad?](#why-is-this-bad)

Stub (`.pyi`) files should use type annotations directly, rather
than type comments, even if they're intended to support Python 2, since
stub files are not executed at runtime. The one exception is `# type: ignore`.

## [Example](#example)

```
x = 1  # type: int
```

Use instead:

```
x: int = 1
```