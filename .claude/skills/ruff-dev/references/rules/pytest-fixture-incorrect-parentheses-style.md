# [pytest-fixture-incorrect-parentheses-style (PT001)](#pytest-fixture-incorrect-parentheses-style-pt001)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-fixture-incorrect-parentheses-style%27%20OR%20PT001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ffixture.rs#L82)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for argument-free `@pytest.fixture()` decorators with or without
parentheses, depending on the [`lint.flake8-pytest-style.fixture-parentheses`](../../settings/#lint_flake8-pytest-style_fixture-parentheses)
setting.

## [Why is this bad?](#why-is-this-bad)

If a `@pytest.fixture()` doesn't take any arguments, the parentheses are
optional.

Either removing those unnecessary parentheses *or* requiring them for all
fixtures is fine, but it's best to be consistent. The rule defaults to
removing unnecessary parentheses, to match the documentation of the
official pytest projects.

## [Example](#example)

```
import pytest


@pytest.fixture()
def my_fixture(): ...
```

Use instead:

```
import pytest


@pytest.fixture
def my_fixture(): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there's comments in the
`pytest.fixture` decorator.

For example, the fix would be marked as unsafe in the following case:

```
import pytest


@pytest.fixture(
    # comment
    # scope = "module"
)
def my_fixture(): ...
```

## [Options](#options)

* [`lint.flake8-pytest-style.fixture-parentheses`](../../settings/#lint_flake8-pytest-style_fixture-parentheses)

## [References](#references)

* [`pytest` documentation: API Reference: Fixtures](https://docs.pytest.org/en/latest/reference/reference.html#fixtures-api)