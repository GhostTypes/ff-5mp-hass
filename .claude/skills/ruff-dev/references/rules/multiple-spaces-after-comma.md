# [multiple-spaces-after-comma (E241)](#multiple-spaces-after-comma-e241)

Preview (since [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-spaces-after-comma%27%20OR%20E241)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fspace_around_operator.rs#L189)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous whitespace after a comma.

## [Why is this bad?](#why-is-this-bad)

Consistency is good. This rule helps ensure you have a consistent
formatting style across your project.

## [Example](#example)

```
a = 4,    5
```

Use instead:

```
a = 4, 5
```