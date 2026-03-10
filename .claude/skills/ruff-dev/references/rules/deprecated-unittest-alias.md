# [deprecated-unittest-alias (UP005)](#deprecated-unittest-alias-up005)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27deprecated-unittest-alias%27%20OR%20UP005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fdeprecated_unittest_alias.rs#L41)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of deprecated methods from the `unittest` module.

## [Why is this bad?](#why-is-this-bad)

The `unittest` module has deprecated aliases for some of its methods.
The deprecated aliases were removed in Python 3.12. Instead of aliases,
use their non-deprecated counterparts.

## [Example](#example)

```
from unittest import TestCase


class SomeTest(TestCase):
    def test_something(self):
        self.assertEquals(1, 1)
```

Use instead:

```
from unittest import TestCase


class SomeTest(TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
```

## [References](#references)

* [Python 3.11 documentation: Deprecated aliases](https://docs.python.org/3.11/library/unittest.html#deprecated-aliases)