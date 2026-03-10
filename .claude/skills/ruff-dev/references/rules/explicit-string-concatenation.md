# [explicit-string-concatenation (ISC003)](#explicit-string-concatenation-isc003)

Added in [v0.0.201](https://github.com/astral-sh/ruff/releases/tag/v0.0.201) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27explicit-string-concatenation%27%20OR%20ISC003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_implicit_str_concat%2Frules%2Fexplicit.rs#L35)

Derived from the **[flake8-implicit-str-concat](../#flake8-implicit-str-concat-isc)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for string literals that are explicitly concatenated (using the
`+` operator).

## [Why is this bad?](#why-is-this-bad)

For string literals that wrap across multiple lines, implicit string
concatenation within parentheses is preferred over explicit
concatenation using the `+` operator, as the former is more readable.

## [Example](#example)

```
z = (
    "The quick brown fox jumps over the lazy "
    + "dog"
)
```

Use instead:

```
z = (
    "The quick brown fox jumps over the lazy "
    "dog"
)
```