# [if-tuple (F634)](#if-tuple-f634)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27if-tuple%27%20OR%20F634)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fif_tuple.rs#L31)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `if` statements that use non-empty tuples as test conditions.

## [Why is this bad?](#why-is-this-bad)

Non-empty tuples are always `True`, so an `if` statement with a non-empty
tuple as its test condition will always pass. This is likely a mistake.

## [Example](#example)

```
if (False,):
    print("This will always run")
```

Use instead:

```
if False:
    print("This will never run")
```

## [References](#references)

* [Python documentation: The `if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)