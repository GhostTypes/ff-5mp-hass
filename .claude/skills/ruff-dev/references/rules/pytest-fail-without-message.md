# [pytest-fail-without-message (PT016)](#pytest-fail-without-message-pt016)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-fail-without-message%27%20OR%20PT016)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffail.rs#L48)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.fail` calls without a message.

## [Why is this bad?](#why-is-this-bad)

`pytest.fail` calls without a message make it harder to understand and debug test failures.

## [Example](#example)

```
import pytest


def test_foo():
    pytest.fail()


def test_bar():
    pytest.fail("")


def test_baz():
    pytest.fail(reason="")
```

Use instead:

```
import pytest


def test_foo():
    pytest.fail("...")


def test_bar():
    pytest.fail(reason="...")
```

## [References](#references)

* [`pytest` documentation: `pytest.fail`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-fail)