# [pytest-extraneous-scope-function (PT003)](#pytest-extraneous-scope-function-pt003)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-extraneous-scope-function%27%20OR%20PT003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L176)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `pytest.fixture` calls with `scope="function"`.

## [Why is this bad?](#why-is-this-bad)

`scope="function"` can be omitted, as it is the default.

## [Example](#example)

```
import pytest


@pytest.fixture(scope="function")
def my_fixture(): ...
```

Use instead:

```
import pytest


@pytest.fixture()
def my_fixture(): ...
```

## [References](#references)

* [`pytest` documentation: `@pytest.fixture` functions](https://docs.pytest.org/en/latest/reference/reference.html#pytest-fixture)