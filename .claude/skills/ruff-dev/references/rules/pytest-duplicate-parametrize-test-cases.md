# [pytest-duplicate-parametrize-test-cases (PT014)](#pytest-duplicate-parametrize-test-cases-pt014)

Added in [v0.0.285](https://github.com/astral-sh/ruff/releases/tag/v0.0.285) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-duplicate-parametrize-test-cases%27%20OR%20PT014)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fparametrize.rs#L267)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for duplicate test cases in `pytest.mark.parametrize`.

## [Why is this bad?](#why-is-this-bad)

Duplicate test cases are redundant and should be removed.

## [Example](#example)

```
import pytest


@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (1, 2),
        (1, 2),
    ],
)
def test_foo(param1, param2): ...
```

Use instead:

```
import pytest


@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (1, 2),
    ],
)
def test_foo(param1, param2): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as tests that rely on mutable global
state may be affected by removing duplicate test cases.

## [References](#references)

* [`pytest` documentation: How to parametrize fixtures and test functions](https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-mark-parametrize)