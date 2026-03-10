# [multiple-with-statements (SIM117)](#multiple-with-statements-sim117)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-with-statements%27%20OR%20SIM117)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fast_with.rs#L49)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the unnecessary nesting of multiple consecutive context
managers.

## [Why is this bad?](#why-is-this-bad)

In Python 3, a single `with` block can include multiple context
managers.

Combining multiple context managers into a single `with` statement
will minimize the indentation depth of the code, making it more
readable.

The following context managers are exempt when used as standalone
statements:

* `anyio`.{`CancelScope`, `fail_after`, `move_on_after`}
* `asyncio`.{`timeout`, `timeout_at`}
* `trio`.{`fail_after`, `fail_at`, `move_on_after`, `move_on_at`}

## [Example](#example)

```
with A() as a:
    with B() as b:
        pass
```

Use instead:

```
with A() as a, B() as b:
    pass
```

## [References](#references)

* [Python documentation: The `with` statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)