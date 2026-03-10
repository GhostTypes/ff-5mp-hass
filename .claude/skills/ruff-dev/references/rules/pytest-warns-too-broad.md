# [pytest-warns-too-broad (PT030)](#pytest-warns-too-broad-pt030)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-warns-too-broad%27%20OR%20PT030)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fwarns.rs#L104)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.warns` calls without a `match` parameter.

## [Why is this bad?](#why-is-this-bad)

`pytest.warns(Warning)` will catch any `Warning` and may catch warnings that
are unrelated to the code under test. To avoid this, `pytest.warns` should
be called with a `match` parameter. The warning names that require a `match`
parameter can be configured via the
[`lint.flake8-pytest-style.warns-require-match-for`](../../settings/#lint_flake8-pytest-style_warns-require-match-for) and
[`lint.flake8-pytest-style.warns-extend-require-match-for`](../../settings/#lint_flake8-pytest-style_warns-extend-require-match-for) settings.

## [Example](#example)

```
import pytest


def test_foo():
    with pytest.warns(Warning):
        ...

    # empty string is also an error
    with pytest.warns(Warning, match=""):
        ...
```

Use instead:

```
import pytest


def test_foo():
    with pytest.warns(Warning, match="expected message"):
        ...
```

## [Options](#options)

* [`lint.flake8-pytest-style.warns-require-match-for`](../../settings/#lint_flake8-pytest-style_warns-require-match-for)
* [`lint.flake8-pytest-style.warns-extend-require-match-for`](../../settings/#lint_flake8-pytest-style_warns-extend-require-match-for)

## [References](#references)

* [`pytest` documentation: `pytest.warns`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-warns)