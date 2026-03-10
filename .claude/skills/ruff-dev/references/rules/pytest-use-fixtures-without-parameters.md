# [pytest-use-fixtures-without-parameters (PT026)](#pytest-use-fixtures-without-parameters-pt026)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-use-fixtures-without-parameters%27%20OR%20PT026)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fmarks.rs#L122)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `@pytest.mark.usefixtures()` decorators that aren't passed any
arguments.

## [Why is this bad?](#why-is-this-bad)

A `@pytest.mark.usefixtures()` decorator that isn't passed any arguments is
useless and should be removed.

## [Example](#example)

```
import pytest


@pytest.mark.usefixtures()
def test_something(): ...
```

Use instead:

```
def test_something(): ...
```

## [References](#references)

* [`pytest` documentation: `pytest.mark.usefixtures`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-mark-usefixtures)