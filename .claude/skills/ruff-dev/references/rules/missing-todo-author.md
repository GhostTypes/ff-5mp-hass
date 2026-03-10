# [missing-todo-author (TD002)](#missing-todo-author-td002)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-todo-author%27%20OR%20TD002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L64)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

## [What it does](#what-it-does)

Checks that a TODO comment includes an author.

## [Why is this bad?](#why-is-this-bad)

Including an author on a TODO provides future readers with context around
the issue. While the TODO author is not always considered responsible for
fixing the issue, they are typically the individual with the most context.

## [Example](#example)

```
# TODO: should assign an author here
```

Use instead

```
# TODO(charlie): now an author is assigned
```