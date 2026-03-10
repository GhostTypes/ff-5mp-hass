# [reraise-no-cause (TRY200)](#reraise-no-cause-try200)

Removed (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27reraise-no-cause%27%20OR%20TRY200)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Freraise_no_cause.rs#L39)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule is identical to [B904](https://docs.astral.sh/ruff/rules/raise-without-from-inside-except/) which should be used instead.

## [What it does](#what-it-does)

Checks for exceptions that are re-raised without specifying the cause via
the `from` keyword.

## [Why is this bad?](#why-is-this-bad)

The `from` keyword sets the `__cause__` attribute of the exception, which
stores the "cause" of the exception. The availability of an exception
"cause" is useful for debugging.

## [Example](#example)

```
def reciprocal(n):
    try:
        return 1 / n
    except ZeroDivisionError:
        raise ValueError()
```

Use instead:

```
def reciprocal(n):
    try:
        return 1 / n
    except ZeroDivisionError as exc:
        raise ValueError() from exc
```

## [References](#references)

* [Python documentation: Exception context](https://docs.python.org/3/library/exceptions.html#exception-context)