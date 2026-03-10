# [useless-semicolon (E703)](#useless-semicolon-e703)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27useless-semicolon%27%20OR%20E703)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fcompound_statements.rs#L88)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for statements that end with an unnecessary semicolon.

## [Why is this bad?](#why-is-this-bad)

A trailing semicolon is unnecessary and should be removed.

## [Example](#example)

```
do_four();  # useless semicolon
```

Use instead:

```
do_four()
```