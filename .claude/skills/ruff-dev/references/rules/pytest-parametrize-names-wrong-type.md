# [pytest-parametrize-names-wrong-type (PT006)](#pytest-parametrize-names-wrong-type-pt006)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-parametrize-names-wrong-type%27%20OR%20PT006)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fparametrize.rs#L67)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the type of parameter names passed to `pytest.mark.parametrize`.

## [Why is this bad?](#why-is-this-bad)

The `argnames` argument of `pytest.mark.parametrize` takes a string or
a sequence of strings. For a single parameter, it's preferable to use a
string. For multiple parameters, it's preferable to use the style
configured via the [`lint.flake8-pytest-style.parametrize-names-type`](../../settings/#lint_flake8-pytest-style_parametrize-names-type) setting.

## [Example](#example)

```
import pytest


# single parameter, always expecting string
@pytest.mark.parametrize(("param",), [1, 2, 3])
def test_foo(param): ...


# multiple parameters, expecting tuple
@pytest.mark.parametrize(["param1", "param2"], [(1, 2), (3, 4)])
def test_bar(param1, param2): ...


# multiple parameters, expecting tuple
@pytest.mark.parametrize("param1,param2", [(1, 2), (3, 4)])
def test_baz(param1, param2): ...
```

Use instead:

```
import pytest


@pytest.mark.parametrize("param", [1, 2, 3])
def test_foo(param): ...


@pytest.mark.parametrize(("param1", "param2"), [(1, 2), (3, 4)])
def test_bar(param1, param2): ...
```

## [Options](#options)

* [`lint.flake8-pytest-style.parametrize-names-type`](../../settings/#lint_flake8-pytest-style_parametrize-names-type)

## [References](#references)

* [`pytest` documentation: How to parametrize fixtures and test functions](https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-mark-parametrize)