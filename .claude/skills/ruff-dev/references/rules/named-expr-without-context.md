# [named-expr-without-context (PLW0131)](#named-expr-without-context-plw0131)

Added in [v0.0.270](https://github.com/astral-sh/ruff/releases/tag/v0.0.270) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27named-expr-without-context%27%20OR%20PLW0131)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnamed_expr_without_context.rs#L27)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of named expressions (e.g., `a := 42`) that can be
replaced by regular assignment statements (e.g., `a = 42`).

## [Why is this bad?](#why-is-this-bad)

While a top-level named expression is syntactically and semantically valid,
it's less clear than a regular assignment statement. Named expressions are
intended to be used in comprehensions and generator expressions, where
assignment statements are not allowed.

## [Example](#example)

```
(a := 42)
```

Use instead:

```
a = 42
```