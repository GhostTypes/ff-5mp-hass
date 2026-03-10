# [collapsible-else-if (PLR5501)](#collapsible-else-if-plr5501)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27collapsible-else-if%27%20OR%20PLR5501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fcollapsible_else_if.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `else` blocks that consist of a single `if` statement.

## [Why is this bad?](#why-is-this-bad)

If an `else` block contains a single `if` statement, it can be collapsed
into an `elif`, thus reducing the indentation level.

## [Example](#example)

```
def check_sign(value: int) -> None:
    if value > 0:
        print("Number is positive.")
    else:
        if value < 0:
            print("Number is negative.")
        else:
            print("Number is zero.")
```

Use instead:

```
def check_sign(value: int) -> None:
    if value > 0:
        print("Number is positive.")
    elif value < 0:
        print("Number is negative.")
    else:
        print("Number is zero.")
```

## [References](#references)

* [Python documentation: `if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)