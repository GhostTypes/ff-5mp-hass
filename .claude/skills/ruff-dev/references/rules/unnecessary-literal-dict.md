# [unnecessary-literal-dict (C406)](#unnecessary-literal-dict-c406)

Added in [v0.0.61](https://github.com/astral-sh/ruff/releases/tag/v0.0.61) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-literal-dict%27%20OR%20C406)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_literal_dict.rs#L35)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary list or tuple literals.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a list or tuple literal within a call to `dict()`.
It can be rewritten as a dict literal (`{}`).

## [Example](#example)

```
dict([(1, 2), (3, 4)])
dict(((1, 2), (3, 4)))
dict([])
```

Use instead:

```
{1: 2, 3: 4}
{1: 2, 3: 4}
{}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.