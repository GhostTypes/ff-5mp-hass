# [pytest-incorrect-pytest-import (PT013)](#pytest-incorrect-pytest-import-pt013)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27pytest-incorrect-pytest-import%27%20OR%20PT013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pytest_style%2Frules%2Fimports.rs#L25)

Derived from the **[flake8-pytest-style](../#flake8-pytest-style-pt)** linter.

## [What it does](#what-it-does)

Checks for incorrect import of pytest.

## [Why is this bad?](#why-is-this-bad)

For consistency, `pytest` should be imported as `import pytest` and its members should be
accessed in the form of `pytest.xxx.yyy` for consistency

## [Example](#example)

```
import pytest as pt
from pytest import fixture
```

Use instead:

```
import pytest
```