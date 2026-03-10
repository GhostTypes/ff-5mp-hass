# [decimal-from-float-literal (RUF032)](#decimal-from-float-literal-ruf032)

Added in [0.9.0](https://github.com/astral-sh/ruff/releases/tag/0.9.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27decimal-from-float-literal%27%20OR%20RUF032)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fdecimal_from_float_literal.rs#L35)

Fix is always available.

## [What it does](#what-it-does)

Checks for `Decimal` calls passing a float literal.

## [Why is this bad?](#why-is-this-bad)

Float literals have limited precision that can lead to unexpected results.
The `Decimal` class is designed to handle numbers with fixed-point precision,
so a string literal should be used instead.

## [Example](#example)

```
num = Decimal(1.2345)
```

Use instead:

```
num = Decimal("1.2345")
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because it changes the underlying value
of the `Decimal` instance that is constructed. This can lead to unexpected
behavior if your program relies on the previous value (whether deliberately or not).