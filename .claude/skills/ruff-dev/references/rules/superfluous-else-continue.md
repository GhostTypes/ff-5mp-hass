# [superfluous-else-continue (RET507)](#superfluous-else-continue-ret507)

Added in [v0.0.154](https://github.com/astral-sh/ruff/releases/tag/v0.0.154) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27superfluous-else-continue%27%20OR%20RET507)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_return%2Frules%2Ffunction.rs#L310)

Derived from the **[flake8-return](../#flake8-return-ret)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `else` statements with a `continue` statement in the preceding
`if` block.

## [Why is this bad?](#why-is-this-bad)

The `else` statement is not needed, as the `continue` statement will always
continue onto the next iteration of a loop. Removing the `else` will reduce
nesting and make the code more readable.

## [Example](#example)

```
def foo(bar, baz):
    for i in bar:
        if i < baz:
            continue
        else:
            x = 0
```

Use instead:

```
def foo(bar, baz):
    for i in bar:
        if i < baz:
            continue
        x = 0
```