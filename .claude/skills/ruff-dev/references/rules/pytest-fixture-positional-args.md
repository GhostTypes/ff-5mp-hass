# [pytest-fixture-positional-args (PT002)](#pytest-fixture-positional-args-pt002)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-fixture-positional-args%27%20OR%20PT002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L134)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.fixture` calls with positional arguments.

## [Why is this bad?](#why-is-this-bad)

For clarity and consistency, prefer using keyword arguments to specify
fixture configuration.

## [Example](#example)

```
import pytest


@pytest.fixture("module")
def my_fixture(): ...
```

Use instead:

```
import pytest


@pytest.fixture(scope="module")
def my_fixture(): ...
```

## [References](#references)

* [`pytest` documentation: `@pytest.fixture` functions](https://docs.pytest.org/en/latest/reference/reference.html#pytest-fixture)