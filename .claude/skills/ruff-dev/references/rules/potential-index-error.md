# [potential-index-error (PLE0643)](#potential-index-error-ple0643)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27potential-index-error%27%20OR%20PLE0643)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fpotential_index_error.rs#L21)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for hard-coded sequence accesses that are known to be out of bounds.

## [Why is this bad?](#why-is-this-bad)

Attempting to access a sequence with an out-of-bounds index will cause an
`IndexError` to be raised at runtime. When the sequence and index are
defined statically (e.g., subscripts on `list` and `tuple` literals, with
integer indexes), such errors can be detected ahead of time.

## [Example](#example)

```
print([0, 1, 2][3])
```