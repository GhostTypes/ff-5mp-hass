# [pytest-fixture-param-without-value (PT019)](#pytest-fixture-param-without-value-pt019)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-fixture-param-without-value%27%20OR%20PT019)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L366)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest` test functions that should be decorated with
`@pytest.mark.usefixtures`.

## [Why is this bad?](#why-is-this-bad)

In `pytest`, fixture injection is used to activate fixtures in a test
function.

Fixtures can be injected either by passing them as parameters to the test
function, or by using the `@pytest.mark.usefixtures` decorator.

If the test function depends on the fixture being activated, but does not
use it in the test body or otherwise rely on its return value, prefer
the `@pytest.mark.usefixtures` decorator, to make the dependency explicit
and avoid the confusion caused by unused arguments.

## [Example](#example)

```
import pytest


@pytest.fixture
def _patch_something(): ...


def test_foo(_patch_something): ...
```

Use instead:

```
import pytest


@pytest.fixture
def _patch_something(): ...


@pytest.mark.usefixtures("_patch_something")
def test_foo(): ...
```

## [References](#references)

* [`pytest` documentation: `pytest.mark.usefixtures`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-mark-usefixtures)