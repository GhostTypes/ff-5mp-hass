# [pytest-parameter-with-default-argument (PT028)](#pytest-parameter-with-default-argument-pt028)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-parameter-with-default-argument%27%20OR%20PT028)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Ftest_functions.rs#L33)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for parameters of test functions with default arguments.

## [Why is this bad?](#why-is-this-bad)

Such a parameter will always have the default value during the test
regardless of whether a fixture with the same name is defined.

## [Example](#example)

```
def test_foo(a=1): ...
```

Use instead:

```
def test_foo(a): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as modifying a function signature can
change the behavior of the code.

## [References](#references)

* [Original Pytest issue](https://github.com/pytest-dev/pytest/issues/12693)