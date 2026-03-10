# [extraneous-parentheses (UP034)](#extraneous-parentheses-up034)

Added in [v0.0.228](https://github.com/astral-sh/ruff/releases/tag/v0.0.228) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27extraneous-parentheses%27%20OR%20UP034)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fextraneous_parentheses.rs#L27)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for extraneous parentheses.

## [Why is this bad?](#why-is-this-bad)

Extraneous parentheses are redundant, and can be removed to improve
readability while retaining identical semantics.

## [Example](#example)

```
print(("Hello, world"))
```

Use instead:

```
print("Hello, world")
```