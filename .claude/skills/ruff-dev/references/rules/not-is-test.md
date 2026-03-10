# [not-is-test (E714)](#not-is-test-e714)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27not-is-test%27%20OR%20E714)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fnot_tests.rs#L67)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for identity comparisons using `not {foo} is {bar}`.

## [Why is this bad?](#why-is-this-bad)

According to [PEP8](https://peps.python.org/pep-0008/#programming-recommendations), testing for an object's identity with `is not` is more
readable.

## [Example](#example)

```
if not X is Y:
    pass
Z = not X.B is Y
```

Use instead:

```
if X is not Y:
    pass
Z = X.B is not Y
```