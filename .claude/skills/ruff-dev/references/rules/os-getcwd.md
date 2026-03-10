# [os-getcwd (PTH109)](#os-getcwd-pth109)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-getcwd%27%20OR%20PTH109)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_getcwd.rs#L53)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.getcwd` and `os.getcwdb`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os`. When possible, using `Path` object
methods such as `Path.cwd()` can improve readability over the `os`
module's counterparts (e.g., `os.getcwd()`).

## [Examples](#examples)

```
import os

cwd = os.getcwd()
```

Use instead:

```
from pathlib import Path

cwd = Path.cwd()
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.
Additionally, the fix is marked as unsafe when the return value is used because the type changes
from `str` or `bytes` to a `Path` object.

## [References](#references)

* [Python documentation: `Path.cwd`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd)
* [Python documentation: `os.getcwd`](https://docs.python.org/3/library/os.html#os.getcwd)
* [Python documentation: `os.getcwdb`](https://docs.python.org/3/library/os.html#os.getcwdb)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)