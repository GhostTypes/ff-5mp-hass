# [unnecessary-list-call (C411)](#unnecessary-list-call-c411)

Added in [v0.0.73](https://github.com/astral-sh/ruff/releases/tag/v0.0.73) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-list-call%27%20OR%20C411)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_list_call.rs#L31)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `list()` calls around list comprehensions.

## [Why is this bad?](#why-is-this-bad)

It is redundant to use a `list()` call around a list comprehension.

## [Example](#example)

```
list([f(x) for x in foo])
```

Use instead

```
[f(x) for x in foo]
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.