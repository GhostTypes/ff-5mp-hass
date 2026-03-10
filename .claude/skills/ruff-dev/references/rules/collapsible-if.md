# [collapsible-if (SIM102)](#collapsible-if-sim102)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27collapsible-if%27%20OR%20SIM102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fcollapsible_if.rs#L48)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for nested `if` statements that can be collapsed into a single `if`
statement.

## [Why is this bad?](#why-is-this-bad)

Nesting `if` statements leads to deeper indentation and makes code harder to
read. Instead, combine the conditions into a single `if` statement with an
`and` operator.

## [Example](#example)

```
if foo:
    if bar:
        ...
```

Use instead:

```
if foo and bar:
    ...
```

## [References](#references)

* [Python documentation: The `if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)
* [Python documentation: Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)