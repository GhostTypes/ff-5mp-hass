# [assert-on-string-literal (PLW0129)](#assert-on-string-literal-plw0129)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert-on-string-literal%27%20OR%20PLW0129)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fassert_on_string_literal.rs#L28)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `assert` statements that use a string literal as the first
argument.

## [Why is this bad?](#why-is-this-bad)

An `assert` on a non-empty string literal will always pass, while an
`assert` on an empty string literal will always fail.

## [Example](#example)

```
assert "always true"
```