# [assert-false (B011)](#assert-false-b011)

Added in [v0.0.67](https://github.com/astral-sh/ruff/releases/tag/v0.0.67) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert-false%27%20OR%20B011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fassert_false.rs#L37)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `assert False`.

## [Why is this bad?](#why-is-this-bad)

Python removes `assert` statements when running in optimized mode
(`python -O`), making `assert False` an unreliable means of
raising an `AssertionError`.

Instead, raise an `AssertionError` directly.

## [Example](#example)

```
assert False
```

Use instead:

```
raise AssertionError
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as changing an `assert` to a
`raise` will change the behavior of your program when running in
optimized mode (`python -O`).

## [References](#references)

* [Python documentation: `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)