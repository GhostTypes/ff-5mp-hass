# [useless-else-on-loop (PLW0120)](#useless-else-on-loop-plw0120)

Added in [v0.0.156](https://github.com/astral-sh/ruff/releases/tag/v0.0.156) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-else-on-loop%27%20OR%20PLW0120)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fuseless_else_on_loop.rs#L49)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `else` clauses on loops without a `break` statement.

## [Why is this bad?](#why-is-this-bad)

When a loop includes an `else` statement, the code inside the `else` clause
will be executed if the loop terminates "normally" (i.e., without a
`break`).

If a loop *always* terminates "normally" (i.e., does *not* contain a
`break`), then the `else` clause is redundant, as the code inside the
`else` clause will always be executed.

In such cases, the code inside the `else` clause can be moved outside the
loop entirely, and the `else` clause can be removed.

## [Example](#example)

```
for item in items:
    print(item)
else:
    print("All items printed")
```

Use instead:

```
for item in items:
    print(item)
print("All items printed")
```

## [References](#references)

* [Python documentation: `break` and `continue` Statements, and `else` Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)