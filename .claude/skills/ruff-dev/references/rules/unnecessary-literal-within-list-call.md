# [unnecessary-literal-within-list-call (C410)](#unnecessary-literal-within-list-call-c410)

Added in [v0.0.66](https://github.com/astral-sh/ruff/releases/tag/v0.0.66) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-literal-within-list-call%27%20OR%20C410)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_literal_within_list_call.rs#L37)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `list()` calls that take unnecessary list or tuple literals as
arguments.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to use a list or tuple literal within a `list()` call,
since there is a literal syntax for these types.

If a list literal is passed in, then the outer call to `list()` should be
removed. Otherwise, if a tuple literal is passed in, then it should be
rewritten as a list literal.

## [Example](#example)

```
list([1, 2])
list((1, 2))
```

Use instead:

```
[1, 2]
[1, 2]
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.