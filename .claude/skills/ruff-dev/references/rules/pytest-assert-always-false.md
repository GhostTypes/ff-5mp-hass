# [pytest-assert-always-false (PT015)](#pytest-assert-always-false-pt015)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-assert-always-false%27%20OR%20PT015)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fassertion.rs#L153)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `assert` statements whose test expression is a falsy value.

## [Why is this bad?](#why-is-this-bad)

`pytest.fail` conveys the intent more clearly than `assert falsy_value`.

## [Example](#example)

```
def test_foo():
    if some_condition:
        assert False, "some_condition was True"
```

Use instead:

```
import pytest


def test_foo():
    if some_condition:
        pytest.fail("some_condition was True")
    ...
```

## [References](#references)

* [`pytest` documentation: `pytest.fail`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-fail)