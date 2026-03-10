# [unnecessary-literal-within-dict-call (C418)](#unnecessary-literal-within-dict-call-c418)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-literal-within-dict-call%27%20OR%20C418)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_comprehensions%2Frules%2Funnecessary_literal_within_dict_call.rs#L37)

Derived from the **[flake8-comprehensions](../#flake8-comprehensions-c4)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `dict()` calls that take unnecessary dict literals or dict
comprehensions as arguments.

## [Why is this bad?](#why-is-this-bad)

It's unnecessary to wrap a dict literal or comprehension within a `dict()`
call, since the literal or comprehension syntax already returns a
dictionary.

## [Example](#example)

```
dict({})
dict({"a": 1})
```

Use instead:

```
{}
{"a": 1}
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.