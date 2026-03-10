# [unnecessary-list-comprehension-set (C403)](#unnecessary-list-comprehension-set-c403)

Added in [v0.0.58](https://github.com/astral-sh/ruff/releases/tag/v0.0.58) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-list-comprehension-set%27%20OR%20C403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_list_comprehension_set.rs#L33)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary list comprehensions.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a list comprehension inside a call to `set()`,
since there is an equivalent comprehension for this type.

## [Example](#example)

```
set([f(x) for x in foo])
```

Use instead:

```
{f(x) for x in foo}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.