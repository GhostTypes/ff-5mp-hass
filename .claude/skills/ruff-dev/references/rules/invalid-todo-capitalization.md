# [invalid-todo-capitalization (TD006)](#invalid-todo-capitalization-td006)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-todo-capitalization%27%20OR%20TD006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L192)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks that a "TODO" tag is properly capitalized (i.e., that the tag is
uppercase).

## [Why is this bad?](#why-is-this-bad)

Capitalizing the "TODO" in a TODO comment is a convention that makes it
easier for future readers to identify TODOs.

## [Example](#example)

```
# todo(charlie): capitalize this
```

Use instead:

```
# TODO(charlie): this is capitalized
```