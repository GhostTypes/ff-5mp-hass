# [yoda-conditions (SIM300)](#yoda-conditions-sim300)

Added in [v0.0.207](https://github.com/astral-sh/ruff/releases/tag/v0.0.207) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27yoda-conditions%27%20OR%20SIM300)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fyoda_conditions.rs#L50)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for conditions that position a constant on the left-hand side of the
comparison operator, rather than the right-hand side.

## [Why is this bad?](#why-is-this-bad)

These conditions (sometimes referred to as "Yoda conditions") are less
readable than conditions that place the variable on the left-hand side of
the comparison operator.

In some languages, Yoda conditions are used to prevent accidental
assignment in conditions (i.e., accidental uses of the `=` operator,
instead of the `==` operator). However, Python does not allow assignments
in conditions unless using the `:=` operator, so Yoda conditions provide
no benefit in this regard.

## [Example](#example)

```
if "Foo" == foo:
    ...
```

Use instead:

```
if foo == "Foo":
    ...
```

## [References](#references)

* [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
* [Python documentation: Assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)