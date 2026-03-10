# [no-indented-block (E112)](#no-indented-block-e112)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-indented-block%27%20OR%20E112)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Findentation.rs#L120)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for indented blocks that are lacking indentation.

## [Why is this bad?](#why-is-this-bad)

All indented blocks should be indented; otherwise, they are not valid
Python syntax.

## [Example](#example)

```
for item in items:
pass
```

Use instead:

```
for item in items:
    pass
```