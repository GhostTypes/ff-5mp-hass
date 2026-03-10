# [return-in-try-except-finally (SIM107)](#return-in-try-except-finally-sim107)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27return-in-try-except-finally%27%20OR%20SIM107)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Freturn_in_try_except_finally.rs#L43)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

## [What it does](#what-it-does)

Checks for `return` statements in `try`-`except` and `finally` blocks.

## [Why is this bad?](#why-is-this-bad)

The `return` statement in a `finally` block will always be executed, even if
an exception is raised in the `try` or `except` block. This can lead to
unexpected behavior.

## [Example](#example)

```
def squared(n):
    try:
        sqr = n**2
        return sqr
    except Exception:
        return "An exception occurred"
    finally:
        return -1  # Always returns -1.
```

Use instead:

```
def squared(n):
    try:
        return_value = n**2
    except Exception:
        return_value = "An exception occurred"
    finally:
        return_value = -1
    return return_value
```

## [References](#references)

* [Python documentation: Defining Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)