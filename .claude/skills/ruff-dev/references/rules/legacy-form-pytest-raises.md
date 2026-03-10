# [legacy-form-pytest-raises (RUF061)](#legacy-form-pytest-raises-ruf061)

Preview (since [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27legacy-form-pytest-raises%27%20OR%20RUF061)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Flegacy_form_pytest_raises.rs#L46)

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for non-contextmanager use of `pytest.raises`, `pytest.warns`, and `pytest.deprecated_call`.

## [Why is this bad?](#why-is-this-bad)

The context-manager form is more readable, easier to extend, and supports additional kwargs.

## [Example](#example)

```
import pytest


excinfo = pytest.raises(ValueError, int, "hello")
pytest.warns(UserWarning, my_function, arg)
pytest.deprecated_call(my_deprecated_function, arg1, arg2)
```

Use instead:

```
import pytest


with pytest.raises(ValueError) as excinfo:
    int("hello")
with pytest.warns(UserWarning):
    my_function(arg)
with pytest.deprecated_call():
    my_deprecated_function(arg1, arg2)
```

## [References](#references)

* [`pytest` documentation: `pytest.raises`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-raises)
* [`pytest` documentation: `pytest.warns`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-warns)
* [`pytest` documentation: `pytest.deprecated_call`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-deprecated-call)