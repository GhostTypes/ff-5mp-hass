# [pytest-raises-too-broad (PT011)](#pytest-raises-too-broad-pt011)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-raises-too-broad%27%20OR%20PT011)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fraises.rs#L105)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `pytest.raises` calls without a `match` parameter.

## [Why is this bad?](#why-is-this-bad)

`pytest.raises(Error)` will catch any `Error` and may catch errors that are
unrelated to the code under test. To avoid this, `pytest.raises` should be
called with a `match` parameter. The exception names that require a `match`
parameter can be configured via the
[`lint.flake8-pytest-style.raises-require-match-for`](../../settings/#lint_flake8-pytest-style_raises-require-match-for) and
[`lint.flake8-pytest-style.raises-extend-require-match-for`](../../settings/#lint_flake8-pytest-style_raises-extend-require-match-for) settings.

## [Example](#example)

```
import pytest


def test_foo():
    with pytest.raises(ValueError):
        ...

    # empty string is also an error
    with pytest.raises(ValueError, match=""):
        ...
```

Use instead:

```
import pytest


def test_foo():
    with pytest.raises(ValueError, match="expected message"):
        ...
```

## [Options](#options)

* [`lint.flake8-pytest-style.raises-require-match-for`](../../settings/#lint_flake8-pytest-style_raises-require-match-for)
* [`lint.flake8-pytest-style.raises-extend-require-match-for`](../../settings/#lint_flake8-pytest-style_raises-extend-require-match-for)

## [References](#references)

* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)