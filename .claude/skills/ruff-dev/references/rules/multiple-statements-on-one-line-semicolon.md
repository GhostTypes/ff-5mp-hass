# [multiple-statements-on-one-line-semicolon (E702)](#multiple-statements-on-one-line-semicolon-e702)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-statements-on-one-line-semicolon%27%20OR%20E702)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fcompound_statements.rs#L62)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for multiline statements on one line.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#other-recommendations), including multi-clause statements on the same line is
discouraged.

## [Example](#example)

```
do_one(); do_two(); do_three()
```

Use instead:

```
do_one()
do_two()
do_three()
```