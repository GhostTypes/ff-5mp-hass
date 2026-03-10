# [useless-exception-statement (PLW0133)](#useless-exception-statement-plw0133)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-exception-statement%27%20OR%20PLW0133)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fuseless_exception_statement.rs#L41)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for an exception that is not raised.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to create an exception without raising it. For example,
`ValueError("...")` on its own will have no effect (unlike
`raise ValueError("...")`) and is likely a mistake.

## [Known problems](#known-problems)

This rule only detects built-in exceptions, like `ValueError`, and does
not catch user-defined exceptions.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also detect user-defined exceptions, but only
the ones defined in the file being checked.

## [Example](#example)

```
ValueError("...")
```

Use instead:

```
raise ValueError("...")
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as converting a useless exception