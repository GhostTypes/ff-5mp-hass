# [pytest-unnecessary-asyncio-mark-on-fixture (PT024)](#pytest-unnecessary-asyncio-mark-on-fixture-pt024)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-unnecessary-asyncio-mark-on-fixture%27%20OR%20PT024)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L626)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `@pytest.mark.asyncio` decorators applied to fixtures.

## [Why is this bad?](#why-is-this-bad)

`pytest.mark.asyncio` is unnecessary for fixtures.

## [Example](#example)

```
import pytest


@pytest.mark.asyncio()
@pytest.fixture()
async def my_fixture():
    return 0
```

Use instead:

```
import pytest


@pytest.fixture()
async def my_fixture():
    return 0
```

## [References](#references)

* [PyPI: `pytest-asyncio`](https://pypi.org/project/pytest-asyncio/)