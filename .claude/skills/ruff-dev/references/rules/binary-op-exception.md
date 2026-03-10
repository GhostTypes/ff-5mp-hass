# [binary-op-exception (PLW0711)](#binary-op-exception-plw0711)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27binary-op-exception%27%20OR%20PLW0711)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbinary_op_exception.rs#L49)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `except` clauses that attempt to catch multiple
exceptions with a binary operation (`and` or `or`).

## [Why is this bad?](#why-is-this-bad)

A binary operation will not catch multiple exceptions. Instead, the binary
operation will be evaluated first, and the result of *that* operation will
be caught (for an `or` operation, this is typically the first exception in
the list). This is almost never the desired behavior.

## [Example](#example)

```
try:
    pass
except A or B:
    pass
```

Use instead:

```
try:
    pass
except (A, B):
    pass
```