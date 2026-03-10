# [pytest-composite-assertion (PT018)](#pytest-composite-assertion-pt018)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-composite-assertion%27%20OR%20PT018)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fassertion.rs#L63)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for assertions that combine multiple independent conditions.

## [Why is this bad?](#why-is-this-bad)

Composite assertion statements are harder to debug upon failure, as the
failure message will not indicate which condition failed.

## [Example](#example)

```
def test_foo():
    assert something and something_else


def test_bar():
    assert not (something or something_else)
```

Use instead:

```
def test_foo():
    assert something
    assert something_else


def test_bar():
    assert not something
    assert not something_else
```