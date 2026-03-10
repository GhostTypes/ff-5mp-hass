# [assert (S101)](#assert-s101)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert%27%20OR%20S101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fassert_used.rs#L35)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the `assert` keyword.

## [Why is this bad?](#why-is-this-bad)

Assertions are removed when Python is run with optimization requested
(i.e., when the `-O` flag is present), which is a common practice in
production environments. As such, assertions should not be used for runtime
validation of user input or to enforce interface constraints.

Consider raising a meaningful error instead of using `assert`.

## [Example](#example)

```
assert x > 0, "Expected positive value."
```

Use instead:

```
if not x > 0:
    raise ValueError("Expected positive value.")

# or even better:
if x <= 0:
    raise ValueError("Expected positive value.")
```