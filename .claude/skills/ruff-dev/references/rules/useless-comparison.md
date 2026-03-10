# [useless-comparison (B015)](#useless-comparison-b015)

Added in [v0.0.102](https://github.com/astral-sh/ruff/releases/tag/v0.0.102) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-comparison%27%20OR%20B015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fuseless_comparison.rs#L36)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for useless comparisons.

## [Why is this bad?](#why-is-this-bad)

Useless comparisons have no effect on the program, and are often included
by mistake. If the comparison is intended to enforce an invariant, prepend
the comparison with an `assert`. Otherwise, remove it entirely.

## [Example](#example)

```
foo == bar
```

Use instead:

```
assert foo == bar, "`foo` and `bar` should be equal."
```

## [Notebook behavior](#notebook-behavior)

For Jupyter Notebooks, this rule is not applied to the last top-level expression in a cell.
This is because it's common to have a notebook cell that ends with an expression,
which will result in the `repr` of the evaluated expression being printed as the cell's output.

## [References](#references)

* [Python documentation: `assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)