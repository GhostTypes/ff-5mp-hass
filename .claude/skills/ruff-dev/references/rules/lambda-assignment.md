# [lambda-assignment (E731)](#lambda-assignment-e731)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27lambda-assignment%27%20OR%20E731)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flambda_assignment.rs#L38)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for lambda expressions which are assigned to a variable.

## [Why is this bad?](#why-is-this-bad)

Per PEP 8, you should "Always use a def statement instead of an assignment
statement that binds a lambda expression directly to an identifier."

Using a `def` statement leads to better tracebacks, and the assignment
itself negates the primary benefit of using a `lambda` expression (i.e.,
that it can be embedded inside another expression).

## [Example](#example)

```
f = lambda x: 2 * x
```

Use instead:

```
def f(x):
    return 2 * x
```