# [assert-tuple (F631)](#assert-tuple-f631)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert-tuple%27%20OR%20F631)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fassert_tuple.rs#L30)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `assert` statements that use non-empty tuples as test
conditions.

## [Why is this bad?](#why-is-this-bad)

Non-empty tuples are always `True`, so an `assert` statement with a
non-empty tuple as its test condition will always pass. This is likely a
mistake.

## [Example](#example)

```
assert (some_condition,)
```

Use instead:

```
assert some_condition
```

## [References](#references)

* [Python documentation: The `assert` statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)