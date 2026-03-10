# [superfluous-else-break (RET508)](#superfluous-else-break-ret508)

Added in [v0.0.154](https://github.com/astral-sh/ruff/releases/tag/v0.0.154) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27superfluous-else-break%27%20OR%20RET508)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_return%2Frules%2Ffunction.rs#L357)

Derived from the **[flake8-return](../#flake8-return-ret)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `else` statements with a `break` statement in the preceding `if`
block.

## [Why is this bad?](#why-is-this-bad)

The `else` statement is not needed, as the `break` statement will always
break out of the loop. Removing the `else` will reduce nesting and make the
code more readable.

## [Example](#example)

```
def foo(bar, baz):
    for i in bar:
        if i > baz:
            break
        else:
            x = 0
```

Use instead:

```
def foo(bar, baz):
    for i in bar:
        if i > baz:
            break
        x = 0
```