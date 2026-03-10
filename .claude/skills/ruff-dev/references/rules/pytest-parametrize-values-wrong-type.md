# [pytest-parametrize-values-wrong-type (PT007)](#pytest-parametrize-values-wrong-type-pt007)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-parametrize-values-wrong-type%27%20OR%20PT007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fparametrize.rs#L202)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for the type of parameter values passed to `pytest.mark.parametrize`.

## [Why is this bad?](#why-is-this-bad)

The `argvalues` argument of `pytest.mark.parametrize` takes an iterator of
parameter values, which can be provided as lists or tuples.

To aid in readability, it's recommended to use a consistent style for the
list of values rows, and, in the case of multiple parameters, for each row
of values.

The style for the list of values rows can be configured via the
[`lint.flake8-pytest-style.parametrize-values-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-type) setting, while the
style for each row of values can be configured via the
[`lint.flake8-pytest-style.parametrize-values-row-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-row-type) setting.

For example, [`lint.flake8-pytest-style.parametrize-values-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-type) will lead to
the following expectations:

* `tuple`: `@pytest.mark.parametrize("value", ("a", "b", "c"))`
* `list`: `@pytest.mark.parametrize("value", ["a", "b", "c"])`

Similarly, [`lint.flake8-pytest-style.parametrize-values-row-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-row-type) will lead to
the following expectations:

* `tuple`: `@pytest.mark.parametrize(("key", "value"), [("a", "b"), ("c", "d")])`
* `list`: `@pytest.mark.parametrize(("key", "value"), [["a", "b"], ["c", "d"]])`

## [Example](#example)

```
import pytest


# expected list, got tuple
@pytest.mark.parametrize("param", (1, 2))
def test_foo(param): ...


# expected top-level list, got tuple
@pytest.mark.parametrize(
    ("param1", "param2"),
    (
        (1, 2),
        (3, 4),
    ),
)
def test_bar(param1, param2): ...


# expected individual rows to be tuples, got lists
@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        [1, 2],
        [3, 4],
    ],
)
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

* [`lint.flake8-pytest-style.parametrize-values-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-type)
* [`lint.flake8-pytest-style.parametrize-values-row-type`](../../settings/#lint_flake8-pytest-style_parametrize-values-row-type)

## [References](#references)

* [`pytest` documentation: How to parametrize fixtures and test functions](https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-mark-parametrize)