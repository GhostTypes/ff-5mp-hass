# [redundant-backslash (E502)](#redundant-backslash-e502)

Preview (since [v0.3.3](https://github.com/astral-sh/ruff/releases/tag/v0.3.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27redundant-backslash%27%20OR%20E502)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fredundant_backslash.rs#L32)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for redundant backslashes between brackets.

## [Why is this bad?](#why-is-this-bad)

Explicit line joins using a backslash are redundant between brackets.

## [Example](#example)

```
x = (2 + \
    2)
```

Use instead:

```
x = (2 +
    2)
```