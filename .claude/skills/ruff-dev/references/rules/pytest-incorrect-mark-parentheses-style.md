# [pytest-incorrect-mark-parentheses-style (PT023)](#pytest-incorrect-mark-parentheses-style-pt023)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-incorrect-mark-parentheses-style%27%20OR%20PT023)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fmarks.rs#L66)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for argument-free `@pytest.mark.<marker>()` decorators with or
without parentheses, depending on the [`lint.flake8-pytest-style.mark-parentheses`](../../settings/#lint_flake8-pytest-style_mark-parentheses)
setting.

The rule defaults to removing unnecessary parentheses,
to match the documentation of the official pytest projects.

## [Why is this bad?](#why-is-this-bad)

If a `@pytest.mark.<marker>()` doesn't take any arguments, the parentheses are
optional.

Either removing those unnecessary parentheses *or* requiring them for all
fixtures is fine, but it's best to be consistent.

## [Example](#example)

```
import pytest


@pytest.mark.foo()
def test_something(): ...
```

Use instead:

```
import pytest


@pytest.mark.foo
def test_something(): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there's comments in the
`pytest.mark.<marker>` decorator.

```
import pytest


@pytest.mark.foo(
    # comment
)
def test_something(): ...
```

## [Options](#options)

* [`lint.flake8-pytest-style.mark-parentheses`](../../settings/#lint_flake8-pytest-style_mark-parentheses)

## [References](#references)

* [`pytest` documentation: Marks](https://docs.pytest.org/en/latest/reference/reference.html#marks)