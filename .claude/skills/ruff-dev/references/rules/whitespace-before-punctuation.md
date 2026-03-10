# [whitespace-before-punctuation (E203)](#whitespace-before-punctuation-e203)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27whitespace-before-punctuation%27%20OR%20E203)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fextraneous_whitespace.rs#L111)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for the use of extraneous whitespace before ",", ";" or ":".

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#pet-peeves) recommends the omission of whitespace in the following cases:

* "Immediately inside parentheses, brackets or braces."
* "Immediately before a comma, semicolon, or colon."

## [Example](#example)

```
if x == 4: print(x, y); x, y = y , x
```

Use instead:

```
if x == 4: print(x, y); x, y = y, x
```