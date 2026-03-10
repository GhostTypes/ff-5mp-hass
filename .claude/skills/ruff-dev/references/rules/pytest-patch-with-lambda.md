# [pytest-patch-with-lambda (PT008)](#pytest-patch-with-lambda-pt008)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-patch-with-lambda%27%20OR%20PT008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fpatch.rs#L44)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for mocked calls that use a dummy `lambda` function instead of
`return_value`.

## [Why is this bad?](#why-is-this-bad)

When patching calls, an explicit `return_value` better conveys the intent
than a `lambda` function, assuming the `lambda` does not use the arguments
passed to it.

`return_value` is also robust to changes in the patched function's
signature, and enables additional assertions to verify behavior. For
example, `return_value` allows for verification of the number of calls or
the arguments passed to the patched function via `assert_called_once_with`
and related methods.

## [Example](#example)

```
def test_foo(mocker):
    mocker.patch("module.target", lambda x, y: 7)
```

Use instead:

```
def test_foo(mocker):
    mocker.patch("module.target", return_value=7)

    # If the lambda makes use of the arguments, no diagnostic is emitted.
    mocker.patch("module.other_target", lambda x, y: x)
```

## [References](#references)

* [Python documentation: `unittest.mock.patch`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
* [PyPI: `pytest-mock`](https://pypi.org/project/pytest-mock/)