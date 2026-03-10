# [pytest-warns-without-warning (PT029)](#pytest-warns-without-warning-pt029)

Preview (since [0.9.2](https://github.com/astral-sh/ruff/releases/tag/0.9.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-warns-without-warning%27%20OR%20PT029)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fwarns.rs#L150)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for `pytest.warns` calls without an expected warning.

## [Why is this bad?](#why-is-this-bad)

`pytest.warns` expects to receive an expected warning as its first
argument. If omitted, the `pytest.warns` call will fail at runtime.

## [Example](#example)

```
import pytest


def test_foo():
    with pytest.warns():
        do_something()
```

Use instead:

```
import pytest


def test_foo():
    with pytest.warns(SomeWarning):
        do_something()
```

## [References](#references)

* [`pytest` documentation: `pytest.warns`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-warns)