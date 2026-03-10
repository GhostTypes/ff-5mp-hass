# [multiple-statements-on-one-line-colon (E701)](#multiple-statements-on-one-line-colon-e701)

Added in [v0.0.245](https://github.com/astral-sh/ruff/releases/tag/v0.0.245) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-statements-on-one-line-colon%27%20OR%20E701)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fcompound_statements.rs#L31)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for compound statements (multiple statements on the same line).

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#other-recommendations), "compound statements are generally discouraged".

## [Example](#example)

```
if foo == "blah": do_blah_thing()
```

Use instead:

```
if foo == "blah":
    do_blah_thing()
```