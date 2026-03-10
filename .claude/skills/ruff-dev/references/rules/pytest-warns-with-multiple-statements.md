# [pytest-warns-with-multiple-statements (PT031)](#pytest-warns-with-multiple-statements-pt031)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-warns-with-multiple-statements%27%20OR%20PT031)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fwarns.rs#L52)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.warns` context managers with multiple statements.

This rule allows `pytest.warns` bodies to contain `for`
loops with empty bodies (e.g., `pass` or `...` statements), to test
iterator behavior.

## [Why is this bad?](#why-is-this-bad)

When `pytest.warns` is used as a context manager and contains multiple
statements, it can lead to the test passing when it should instead fail.

A `pytest.warns` context manager should only contain a single
simple statement that triggers the expected warning.

## [Example](#example)

```
import pytest


def test_foo_warns():
    with pytest.warns(Warning):
        setup()  # False negative if setup triggers a warning but foo does not.
        foo()
```

Use instead:

```
import pytest


def test_foo_warns():
    setup()
    with pytest.warns(Warning):
        foo()
```

## [References](#references)

* [`pytest` documentation: `pytest.warns`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-warns)