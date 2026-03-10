# [global-statement (PLW0603)](#global-statement-plw0603)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27global-statement%27%20OR%20PLW0603)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fglobal_statement.rs#L42)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for the use of `global` statements to update identifiers.

## [Why is this bad?](#why-is-this-bad)

Pylint discourages the use of `global` variables as global mutable
state is a common source of bugs and confusing behavior.

## [Example](#example)

```
var = 1


def foo():
    global var  # [global-statement]
    var = 10
    print(var)


foo()
print(var)
```

Use instead:

```
var = 1


def foo():
    var = 10
    print(var)
    return var


var = foo()
print(var)
```