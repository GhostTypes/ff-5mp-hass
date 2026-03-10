# [verbose-raise (TRY201)](#verbose-raise-try201)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27verbose-raise%27%20OR%20TRY201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Fverbose_raise.rs#L38)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for needless exception names in `raise` statements.

## [Why is this bad?](#why-is-this-bad)

It's redundant to specify the exception name in a `raise` statement if the
exception is being re-raised.

## [Example](#example)

```
def foo():
    try:
        ...
    except ValueError as exc:
        raise exc
```

Use instead:

```
def foo():
    try:
        ...
    except ValueError:
        raise
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it doesn't properly handle bound
exceptions that are shadowed between the `except` and `raise` statements.