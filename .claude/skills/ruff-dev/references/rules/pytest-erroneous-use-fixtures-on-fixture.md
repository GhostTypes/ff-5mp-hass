# [pytest-erroneous-use-fixtures-on-fixture (PT025)](#pytest-erroneous-use-fixtures-on-fixture-pt025)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-erroneous-use-fixtures-on-fixture%27%20OR%20PT025)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L582)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `pytest.mark.usefixtures` decorators applied to `pytest`
fixtures.

## [Why is this bad?](#why-is-this-bad)

The `pytest.mark.usefixtures` decorator has no effect on `pytest` fixtures.

## [Example](#example)

```
import pytest


@pytest.fixture()
def a():
    pass


@pytest.mark.usefixtures("a")
@pytest.fixture()
def b(a):
    pass
```

Use instead:

```
import pytest


@pytest.fixture()
def a():
    pass


@pytest.fixture()
def b(a):
    pass
```

## [References](#references)

* [`pytest` documentation: `pytest.mark.usefixtures`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-mark-usefixtures)