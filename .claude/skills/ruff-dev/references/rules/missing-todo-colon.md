# [missing-todo-colon (TD004)](#missing-todo-colon-td004)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-todo-colon%27%20OR%20TD004)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L136)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

## [What it does](#what-it-does)

Checks that a "TODO" tag is followed by a colon.

## [Why is this bad?](#why-is-this-bad)

"TODO" tags are typically followed by a parenthesized author name, a colon,
a space, and a description of the issue, in that order.

Deviating from this pattern can lead to inconsistent and non-idiomatic
comments.

## [Example](#example)

```
# TODO(charlie) fix this colon
```

Used instead:

```
# TODO(charlie): colon fixed
```