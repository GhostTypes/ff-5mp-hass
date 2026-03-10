# [multiple-spaces-before-keyword (E272)](#multiple-spaces-before-keyword-e272)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-spaces-before-keyword%27%20OR%20E272)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fwhitespace_around_keywords.rs#L54)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous whitespace before keywords.

## [Why is this bad?](#why-is-this-bad)

## [Example](#example)

```
x  and y
```

Use instead:

```
x and y
```