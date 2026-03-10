# [pytest-useless-yield-fixture (PT022)](#pytest-useless-yield-fixture-pt022)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-useless-yield-fixture%27%20OR%20PT022)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L524)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `yield` expressions in `pytest` fixtures.

## [Why is this bad?](#why-is-this-bad)

In `pytest` fixtures, the `yield` expression should only be used for fixtures
that include teardown code, to clean up the fixture after the test function
has finished executing.

## [Example](#example)

```
import pytest


@pytest.fixture()
def my_fixture():
    resource = acquire_resource()
    yield resource
```

Use instead:

```
import pytest


@pytest.fixture()
def my_fixture_with_teardown():
    resource = acquire_resource()
    yield resource
    resource.release()


@pytest.fixture()
def my_fixture_without_teardown():
    resource = acquire_resource()
    return resource
```

## [References](#references)

* [`pytest` documentation: Teardown/Cleanup](https://docs.pytest.org/en/latest/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization)