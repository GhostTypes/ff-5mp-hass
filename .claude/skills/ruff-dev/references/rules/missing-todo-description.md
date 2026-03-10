# [missing-todo-description (TD005)](#missing-todo-description-td005)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27missing-todo-description%27%20OR%20TD005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L164)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

## [What it does](#what-it-does)

Checks that a "TODO" tag contains a description of the issue following the
tag itself.

## [Why is this bad?](#why-is-this-bad)

TODO comments should include a description of the issue to provide context
for future readers.

## [Example](#example)

```
# TODO(charlie)
```

Use instead:

```
# TODO(charlie): fix some issue
```