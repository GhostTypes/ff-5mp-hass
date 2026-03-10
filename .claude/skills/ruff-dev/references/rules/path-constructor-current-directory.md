# [path-constructor-current-directory (PTH201)](#path-constructor-current-directory-pth201)

Added in [v0.0.279](https://github.com/astral-sh/ruff/releases/tag/v0.0.279) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27path-constructor-current-directory%27%20OR%20PTH201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fpath_constructor_current_directory.rs#L42)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `pathlib.Path` objects that are initialized with the current
directory.

## [Why is this bad?](#why-is-this-bad)

The `Path()` constructor defaults to the current directory, so passing it
in explicitly (as `"."`) is unnecessary.

## [Example](#example)

```
from pathlib import Path

_ = Path(".")
```

Use instead:

```
from pathlib import Path

_ = Path()
```

## [Fix safety](#fix-safety)

This fix is marked unsafe if there are comments inside the parentheses, as applying
the fix will delete them.

## [References](#references)

* [Python documentation: `Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path)