# [pytest-fixture-finalizer-callback (PT021)](#pytest-fixture-finalizer-callback-pt021)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-fixture-finalizer-callback%27%20OR%20PT021)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L475)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for unnecessary `request.addfinalizer` usages in `pytest` fixtures.

## [Why is this bad?](#why-is-this-bad)

`pytest` offers two ways to perform cleanup in fixture code. The first is
sequential (via the `yield` statement), the second callback-based (via
`request.addfinalizer`).

The sequential approach is more readable and should be preferred, unless
the fixture uses the "factory as fixture" pattern.

## [Example](#example)

```
import pytest


@pytest.fixture()
def my_fixture(request):
    resource = acquire_resource()
    request.addfinalizer(resource.release)
    return resource
```

Use instead:

```
import pytest


@pytest.fixture()
def my_fixture():
    resource = acquire_resource()
    yield resource
    resource.release()


# "factory-as-fixture" pattern
@pytest.fixture()
def my_factory(request):
    def create_resource(arg):
        resource = acquire_resource(arg)
        request.addfinalizer(resource.release)
        return resource

    return create_resource
```

## [References](#references)

* [`pytest` documentation: Adding finalizers directly](https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly)
* [`pytest` documentation: Factories as fixtures](https://docs.pytest.org/en/latest/how-to/fixtures.html#factories-as-fixtures)