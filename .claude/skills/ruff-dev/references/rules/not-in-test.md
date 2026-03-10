# [not-in-test (E713)](#not-in-test-e713)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27not-in-test%27%20OR%20E713)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fnot_tests.rs#L30)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for membership tests using `not {element} in {collection}`.

## [Why is this bad?](#why-is-this-bad)

Testing membership with `{element} not in {collection}` is more readable.

## [Example](#example)

```
Z = not X in Y
if not X.B in Y:
    pass
```

Use instead:

```
Z = X not in Y
if X.B not in Y:
    pass
```