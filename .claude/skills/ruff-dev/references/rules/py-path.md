# [py-path (PTH124)](#py-path-pth124)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27py-path%27%20OR%20PTH124)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Fviolations.rs#L205)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

## [What it does](#what-it-does)

Checks for uses of the `py.path` library.

## [Why is this bad?](#why-is-this-bad)

The `py.path` library is in maintenance mode. Instead, prefer the standard
library's `pathlib` module, or third-party modules like `path` (formerly
`py.path`).

## [Examples](#examples)

```
import py.path

p = py.path.local("/foo/bar").join("baz/qux")
```

Use instead:

```
from pathlib import Path

p = Path("/foo/bar") / "bar" / "qux"
```

## [References](#references)

* [Python documentation: `Pathlib`](https://docs.python.org/3/library/pathlib.html)
* [Path repository](https://github.com/jaraco/path)