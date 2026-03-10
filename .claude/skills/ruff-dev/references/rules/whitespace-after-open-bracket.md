# [whitespace-after-open-bracket (E201)](#whitespace-after-open-bracket-e201)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27whitespace-after-open-bracket%27%20OR%20E201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fextraneous_whitespace.rs#L33)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for the use of extraneous whitespace after "(", "[" or "{".

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#pet-peeves) recommends the omission of whitespace in the following cases:

* "Immediately inside parentheses, brackets or braces."
* "Immediately before a comma, semicolon, or colon."

## [Example](#example)

```
spam( ham[1], {eggs: 2})
spam(ham[ 1], {eggs: 2})
spam(ham[1], { eggs: 2})
```

Use instead:

```
spam(ham[1], {eggs: 2})
```