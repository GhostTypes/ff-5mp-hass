# [raise-literal (B016)](#raise-literal-b016)

Added in [v0.0.102](https://github.com/astral-sh/ruff/releases/tag/v0.0.102) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-literal%27%20OR%20B016)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fraise_literal.rs#L29)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for `raise` statements that raise a literal value.

## [Why is this bad?](#why-is-this-bad)

`raise` must be followed by an exception instance or an exception class,
and exceptions must be instances of `BaseException` or a subclass thereof.
Raising a literal will raise a `TypeError` at runtime.

## [Example](#example)

```
raise "foo"
```

Use instead:

```
raise Exception("foo")
```

## [References](#references)

* [Python documentation: `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)