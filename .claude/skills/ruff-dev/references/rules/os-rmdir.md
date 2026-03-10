# [os-rmdir (PTH106)](#os-rmdir-pth106)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-rmdir%27%20OR%20PTH106)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_rmdir.rs#L50)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.rmdir`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os`. When possible, using `Path` object
methods such as `Path.rmdir()` can improve readability over the `os`
module's counterparts (e.g., `os.rmdir()`).

## [Examples](#examples)

```
import os

os.rmdir("folder/")
```

Use instead:

```
from pathlib import Path

Path("folder/").rmdir()
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.

## [References](#references)

* [Python documentation: `Path.rmdir`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir)
* [Python documentation: `os.rmdir`](https://docs.python.org/3/library/os.html#os.rmdir)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)