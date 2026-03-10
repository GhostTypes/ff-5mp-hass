# [superfluous-else-raise (RET506)](#superfluous-else-raise-ret506)

Added in [v0.0.154](https://github.com/astral-sh/ruff/releases/tag/v0.0.154) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27superfluous-else-raise%27%20OR%20RET506)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_return%2Frules%2Ffunction.rs#L263)

Derived from the **[flake8-return](../#flake8-return-ret)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `else` statements with a `raise` statement in the preceding `if`
block.

## [Why is this bad?](#why-is-this-bad)

The `else` statement is not needed as the `raise` statement will always
break out of the current scope. Removing the `else` will reduce nesting
and make the code more readable.

## [Example](#example)

```
def foo(bar, baz):
    if bar == "Specific Error":
        raise Exception(bar)
    else:
        raise Exception(baz)
```

Use instead:

```
def foo(bar, baz):
    if bar == "Specific Error":
        raise Exception(bar)
    raise Exception(baz)
```