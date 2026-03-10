# [pytest-unittest-raises-assertion (PT027)](#pytest-unittest-raises-assertion-pt027)

Added in [v0.0.285](https://github.com/astral-sh/ruff/releases/tag/v0.0.285) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-unittest-raises-assertion%27%20OR%20PT027)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fassertion.rs#L348)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of exception-related assertion methods from the `unittest`
module.

## [Why is this bad?](#why-is-this-bad)

To enforce the assertion style recommended by `pytest`, `pytest.raises` is
preferred over the exception-related assertion methods in `unittest`, like
`assertRaises`.

## [Example](#example)

```
import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        with self.assertRaises(ValueError):
            raise ValueError("foo")
```

Use instead:

```
import unittest
import pytest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        with pytest.raises(ValueError):
            raise ValueError("foo")
```

## [References](#references)

* [`pytest` documentation: Assertions about expected exceptions](https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions)