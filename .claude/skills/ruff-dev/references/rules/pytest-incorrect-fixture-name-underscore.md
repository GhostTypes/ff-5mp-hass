# [pytest-incorrect-fixture-name-underscore (PT005)](#pytest-incorrect-fixture-name-underscore-pt005)

Removed (since [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-incorrect-fixture-name-underscore%27%20OR%20PT005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L305)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removal](#removal)

This rule has been removed because marking fixtures that do not return a value with an underscore
isn't a practice recommended by the pytest community.

## [What it does](#what-it-does)

Checks for `pytest` fixtures that return a value, but are named with a
leading underscore.

## [Why is this bad?](#why-is-this-bad)

By convention, fixtures that don't return a value should be named with a
leading underscore, while fixtures that do return a value should not.

This rule ignores abstract fixtures.

## [Example](#example)

```
import pytest


@pytest.fixture()
def _some_object():
    return SomeClass()


@pytest.fixture()
def _some_object_with_cleanup():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```

Use instead:

```
import pytest


@pytest.fixture()
def some_object():
    return SomeClass()


@pytest.fixture()
def some_object_with_cleanup():
    obj = SomeClass()
    yield obj
    obj.cleanup()
```

## [References](#references)

* [`pytest` documentation: `@pytest.fixture` functions](https://docs.pytest.org/en/latest/reference/reference.html#pytest-fixture)