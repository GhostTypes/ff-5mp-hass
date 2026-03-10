# [missing-todo-link (TD003)](#missing-todo-link-td003)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-todo-link%27%20OR%20TD003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L106)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

## [What it does](#what-it-does)

Checks that a TODO comment is associated with a link to a relevant issue
or ticket.

## [Why is this bad?](#why-is-this-bad)

Including an issue link near a TODO makes it easier for resolvers
to get context around the issue.

## [Example](#example)

```
# TODO: this link has no issue
```

Use one of these instead:

```
# TODO(charlie): this comment has an issue link
# https://github.com/astral-sh/ruff/issues/3870

# TODO(charlie): this comment has a 3-digit issue code
# 003

# TODO(charlie): https://github.com/astral-sh/ruff/issues/3870
# this comment has an issue link

# TODO(charlie): #003 this comment has a 3-digit issue code
# with leading character `#`

# TODO(charlie): this comment has an issue code (matches the regex `[A-Z]+\-?\d+`)
# SIXCHR-003
```