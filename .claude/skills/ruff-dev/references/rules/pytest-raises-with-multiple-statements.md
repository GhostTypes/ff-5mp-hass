# [pytest-raises-with-multiple-statements (PT012)](#pytest-raises-with-multiple-statements-pt012)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-raises-with-multiple-statements%27%20OR%20PT012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fraises.rs#L53)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.raises` context managers with multiple statements.

This rule allows `pytest.raises` bodies to contain `for`
loops with empty bodies (e.g., `pass` or `...` statements), to test
iterator behavior.

## [Why is this bad?](#why-is-this-bad)

When a `pytest.raises` is used as a context manager and contains multiple
statements, it can lead to the test passing when it actually should fail.

A `pytest.raises` context manager should only contain a single simple
statement that raises the expected exception.

## [Example](#example)

```
import pytest


def test_foo():
    with pytest.raises(MyError):
        setup()
        func_to_test()  # not executed if `setup()` raises `MyError`
        assert foo()  # not executed
```

Use instead:

```
import pytest


def test_foo():
    setup()
    with pytest.raises(MyError):
        func_to_test()
    assert foo()
```

## [References](#references)

* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)