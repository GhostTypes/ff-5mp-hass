# [pytest-assert-in-except (PT017)](#pytest-assert-in-except-pt017)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-assert-in-except%27%20OR%20PT017)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fassertion.rs#L111)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for `assert` statements in `except` clauses.

## [Why is this bad?](#why-is-this-bad)

When testing for exceptions, `pytest.raises()` should be used instead of
`assert` statements in `except` clauses, as it's more explicit and
idiomatic. Further, `pytest.raises()` will fail if the exception is *not*
raised, unlike the `assert` statement.

## [Example](#example)

```
def test_foo():
    try:
        1 / 0
    except ZeroDivisionError as e:
        assert e.args
```

Use instead:

```
import pytest


def test_foo():
    with pytest.raises(ZeroDivisionError) as exc_info:
        1 / 0
    assert exc_info.value.args
```

## [References](#references)

* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)