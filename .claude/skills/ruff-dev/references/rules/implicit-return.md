# [implicit-return (RET503)](#implicit-return-ret503)

Added in [v0.0.154](https://github.com/astral-sh/ruff/releases/tag/v0.0.154) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-return%27%20OR%20RET503)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_return%2Frules%2Ffunction.rs#L139)

Derived from the **[flake8-return](../#flake8-return-ret)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for missing explicit `return` statements at the end of functions
that can return non-`None` values.

## [Why is this bad?](#why-is-this-bad)

The lack of an explicit `return` statement at the end of a function that
can return non-`None` values can cause confusion. Python implicitly returns
`None` if no other return value is present. Adding an explicit
`return None` can make the code more readable by clarifying intent.

## [Example](#example)

```
def foo(bar):
    if not bar:
        return 1
```

Use instead:

```
def foo(bar):
    if not bar:
        return 1
    return None
```