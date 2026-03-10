# [os-path-splitext (PTH122)](#os-path-splitext-pth122)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-path-splitext%27%20OR%20PTH122)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Fviolations.rs#L168)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

## [What it does](#what-it-does)

Checks for uses of `os.path.splitext`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os.path`. When possible, using `Path` object
methods such as `Path.suffix` and `Path.stem` can improve readability over
the `os.path` module's counterparts (e.g., `os.path.splitext()`).

`os.path.splitext()` specifically returns a tuple of the file root and
extension (e.g., given `splitext('/foo/bar.py')`, `os.path.splitext()`
returns `("foo/bar", ".py")`. These outputs can be reconstructed through a
combination of `Path.suffix` (`".py"`), `Path.stem` (`"bar"`), and
`Path.parent` (`"foo"`).

## [Examples](#examples)

```
import os

(root, ext) = os.path.splitext("foo/bar.py")
```

Use instead:

```
from pathlib import Path

path = Path("foo/bar.py")
root = path.parent / path.stem
ext = path.suffix
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [References](#references)

* [Python documentation: `Path.suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix)
* [Python documentation: `Path.suffixes`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffixes)
* [Python documentation: `os.path.splitext`](https://docs.python.org/3/library/os.path.html#os.path.splitext)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)