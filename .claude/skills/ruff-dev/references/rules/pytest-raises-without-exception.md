# [pytest-raises-without-exception (PT010)](#pytest-raises-without-exception-pt010)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-raises-without-exception%27%20OR%20PT010)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fraises.rs#L154)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.raises` calls without an expected exception.

## [Why is this bad?](#why-is-this-bad)

`pytest.raises` expects to receive an expected exception as its first
argument. If omitted, the `pytest.raises` call will fail at runtime.
The rule will also accept calls without an expected exception but with
`match` and/or `check` keyword arguments, which are also valid after
pytest version 8.4.0.

## [Example](#example)

```
import pytest


def test_foo():
    with pytest.raises():
        do_something()
```

Use instead:

```
import pytest


def test_foo():
    with pytest.raises(SomeException):
        do_something()
```

## [References](#references)

* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)