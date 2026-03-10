# [single-line-implicit-string-concatenation (ISC001)](#single-line-implicit-string-concatenation-isc001)

Added in [v0.0.201](https://github.com/astral-sh/ruff/releases/tag/v0.0.201) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27single-line-implicit-string-concatenation%27%20OR%20ISC001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_implicit_str_concat%2Frules%2Fimplicit.rs#L36)

Derived from the **[flake8-implicit-str-concat](../#flake8-implicit-str-concat-isc)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for implicitly concatenated strings on a single line.

## [Why is this bad?](#why-is-this-bad)

While it is valid Python syntax to concatenate multiple string or byte
literals implicitly (via whitespace delimiters), it is unnecessary and
negatively affects code readability.

In some cases, the implicit concatenation may also be unintentional, as
code formatters are capable of introducing single-line implicit
concatenations when collapsing long lines.

## [Example](#example)

```
z = "The quick " "brown fox."
```

Use instead:

```
z = "The quick brown fox."
```