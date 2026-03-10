# [default-except-not-last (F707)](#default-except-not-last-f707)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27default-except-not-last%27%20OR%20F707)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fdefault_except_not_last.rs#L47)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `except` blocks that handle all exceptions, but are not the last
`except` block in a `try` statement.

## [Why is this bad?](#why-is-this-bad)

When an exception is raised within a `try` block, the `except` blocks are
evaluated in order, and the first matching block is executed. If an `except`
block handles all exceptions, but isn't the last block, Python will raise a
`SyntaxError`, as the following blocks would never be executed.

## [Example](#example)

```
def reciprocal(n):
    try:
        reciprocal = 1 / n
    except:
        print("An exception occurred.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        return reciprocal
```

Use instead:

```
def reciprocal(n):
    try:
        reciprocal = 1 / n
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except:
        print("An exception occurred.")
    else:
        return reciprocal
```

## [References](#references)

* [Python documentation: `except` clause](https://docs.python.org/3/reference/compound_stmts.html#except-clause)