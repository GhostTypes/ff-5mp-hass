# [os-path-join (PTH118)](#os-path-join-pth118)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-path-join%27%20OR%20PTH118)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Fviolations.rs#L96)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

## [What it does](#what-it-does)

Checks for uses of `os.path.join`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os.path`. When possible, using `Path` object
methods such as `Path.joinpath()` or the `/` operator can improve
readability over the `os.path` module's counterparts (e.g., `os.path.join()`).

## [Examples](#examples)

```
import os

os.path.join(os.path.join(ROOT_PATH, "folder"), "file.py")
```

Use instead:

```
from pathlib import Path

Path(ROOT_PATH) / "folder" / "file.py"
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [References](#references)

* [Python documentation: `PurePath.joinpath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath)
* [Python documentation: `os.path.join`](https://docs.python.org/3/library/os.path.html#os.path.join)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)