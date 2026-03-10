# [pytest-deprecated-yield-fixture (PT020)](#pytest-deprecated-yield-fixture-pt020)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-deprecated-yield-fixture%27%20OR%20PT020)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L415)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.yield_fixture` usage.

## [Why is this bad?](#why-is-this-bad)

`pytest.yield_fixture` is deprecated. `pytest.fixture` should be used instead.

## [Example](#example)

```
import pytest


@pytest.yield_fixture()
def my_fixture():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```

Use instead:

```
import pytest


@pytest.fixture()
def my_fixture():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```

## [References](#references)

* [`pytest` documentation: `yield_fixture` functions](https://docs.pytest.org/en/latest/yieldfixture.html)