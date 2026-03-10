# [pytest-unittest-assertion (PT009)](#pytest-unittest-assertion-pt009)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-unittest-assertion%27%20OR%20PT009)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fassertion.rs#L193)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of assertion methods from the `unittest` module.

## [Why is this bad?](#why-is-this-bad)

To make use of `pytest`'s assertion rewriting, a regular `assert` statement
is preferred over `unittest`'s assertion methods.

## [Example](#example)

```
import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(a, b)
```

Use instead:

```
import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        assert a == b
```

## [References](#references)

* [`pytest` documentation: Assertion introspection details](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertion-introspection-details)