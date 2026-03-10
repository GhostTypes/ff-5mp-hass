# [unary-prefix-increment-decrement (B002)](#unary-prefix-increment-decrement-b002)

Added in [v0.0.83](https://github.com/astral-sh/ruff/releases/tag/v0.0.83) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unary-prefix-increment-decrement%27%20OR%20B002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Funary_prefix_increment_decrement.rs#L33)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for the attempted use of the unary prefix increment (`++`) or
decrement operator (`--`).

## [Why is this bad?](#why-is-this-bad)

Python does not support the unary prefix increment or decrement operator.
Writing `++n` is equivalent to `+(+(n))` and writing `--n` is equivalent to
`-(-(n))`. In both cases, it is equivalent to `n`.

## [Example](#example)

```
++x
--y
```

Use instead:

```
x += 1
y -= 1
```

## [References](#references)

* [Python documentation: Unary arithmetic and bitwise operations](https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations)
* [Python documentation: Augmented assignment statements](https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements)