# [global-variable-not-assigned (PLW0602)](#global-variable-not-assigned-plw0602)

Added in [v0.0.174](https://github.com/astral-sh/ruff/releases/tag/v0.0.174) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27global-variable-not-assigned%27%20OR%20PLW0602)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fglobal_variable_not_assigned.rs#L42)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `global` variables that are not assigned a value in the current
scope.

## [Why is this bad?](#why-is-this-bad)

The `global` keyword allows an inner scope to modify a variable declared
in the outer scope. If the variable is not modified within the inner scope,
there is no need to use `global`.

## [Example](#example)

```
DEBUG = True


def foo():
    global DEBUG
    if DEBUG:
        print("foo() called")
    ...
```

Use instead:

```
DEBUG = True


def foo():
    if DEBUG:
        print("foo() called")
    ...
```

## [References](#references)

* [Python documentation: The `global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement)