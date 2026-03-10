# [invalid-todo-tag (TD001)](#invalid-todo-tag-td001)

Added in [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-todo-tag%27%20OR%20TD001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_todos%2Frules%2Ftodos.rs#L33)

Derived from the **[flake8-todos](../#flake8-todos-td)** linter.

## [What it does](#what-it-does)

Checks that a TODO comment is labelled with "TODO".

## [Why is this bad?](#why-is-this-bad)

Ambiguous tags reduce code visibility and can lead to dangling TODOs.
For example, if a comment is tagged with "FIXME" rather than "TODO", it may
be overlooked by future readers.

Note that this rule will only flag "FIXME" and "XXX" tags as incorrect.

## [Example](#example)

```
# FIXME(ruff): this should get fixed!
```

Use instead:

```
# TODO(ruff): this is now fixed!
```