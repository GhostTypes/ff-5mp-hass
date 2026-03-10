# [useless-expression (B018)](#useless-expression-b018)

Added in [v0.0.100](https://github.com/astral-sh/ruff/releases/tag/v0.0.100) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-expression%27%20OR%20B018)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fuseless_expression.rs#L53)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for useless expressions.

## [Why is this bad?](#why-is-this-bad)

Useless expressions have no effect on the program, and are often included
by mistake. Assign a useless expression to a variable, or remove it
entirely.

## [Example](#example)

```
1 + 1
```

Use instead:

```
foo = 1 + 1
```

## [Notebook behavior](#notebook-behavior)

For Jupyter Notebooks, this rule is not applied to the last top-level expression in a cell.
This is because it's common to have a notebook cell that ends with an expression,
which will result in the `repr` of the evaluated expression being printed as the cell's output.

## [Known problems](#known-problems)

This rule ignores expression types that are commonly used for their side
effects, such as function calls.

However, if a seemingly useless expression (like an attribute access) is
needed to trigger a side effect, consider assigning it to an anonymous
variable, to indicate that the return value is intentionally ignored.

For example, given:

```
with errors.ExceptionRaisedContext():
    obj.attribute
```

Use instead:

```
with errors.ExceptionRaisedContext():
    _ = obj.attribute
```