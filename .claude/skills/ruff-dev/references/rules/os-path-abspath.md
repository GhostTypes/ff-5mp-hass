# [os-path-abspath (PTH100)](#os-path-abspath-pth100)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-path-abspath%27%20OR%20PTH100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_path_abspath.rs#L59)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.path.abspath`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os.path`. When possible, using `Path` object
methods such as `Path.resolve()` can improve readability over the `os.path`
module's counterparts (e.g., `os.path.abspath()`).

## [Examples](#examples)

```
import os

file_path = os.path.abspath("../path/to/file")
```

Use instead:

```
from pathlib import Path

file_path = Path("../path/to/file").resolve()
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is always marked as unsafe because `Path.resolve()` resolves symlinks, while
`os.path.abspath()` does not. If resolving symlinks is important, you may need to use
`Path.absolute()`. However, `Path.absolute()` also does not remove any `..` components in a
path, unlike `os.path.abspath()` and `Path.resolve()`, so if that specific combination of
behaviors is required, there's no existing `pathlib` alternative. See CPython issue
[#69200](https://github.com/python/cpython/issues/69200).

Additionally, the fix is marked as unsafe because `os.path.abspath()` returns `str` or `bytes` (`AnyStr`),
while `Path.resolve()` returns a `Path` object. This change in return type can break code that uses
the return value.

## [References](#references)

* [Python documentation: `Path.resolve`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve)
* [Python documentation: `os.path.abspath`](https://docs.python.org/3/library/os.path.html#os.path.abspath)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)