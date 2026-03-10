# [syntax-error (E999)](#syntax-error-e999)

Removed (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27syntax-error%27%20OR%20E999)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ferrors.rs#L67)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule has been removed. Syntax errors will
always be shown regardless of whether this rule is selected or not.

## [What it does](#what-it-does)

Checks for code that contains syntax errors.

## [Why is this bad?](#why-is-this-bad)

Code with syntax errors cannot be executed. Such errors are likely a
mistake.

## [Example](#example)

```
x =
```

Use instead:

```
x = 1
```

## [References](#references)

* [Python documentation: Syntax Errors](https://docs.python.org/3/tutorial/errors.html#syntax-errors)