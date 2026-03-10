# [os-path-expanduser (PTH111)](#os-path-expanduser-pth111)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-path-expanduser%27%20OR%20PTH111)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_path_expanduser.rs#L55)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.path.expanduser`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os.path`. When possible, using `Path` object
methods such as `Path.expanduser()` can improve readability over the `os.path`
module's counterparts (e.g., as `os.path.expanduser()`).

## [Examples](#examples)

```
import os

os.path.expanduser("~/films/Monty Python")
```

Use instead:

```
from pathlib import Path

Path("~/films/Monty Python").expanduser()
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is always marked as unsafe because the behaviors of
`os.path.expanduser` and `Path.expanduser` differ when a user's home
directory can't be resolved: `os.path.expanduser` returns the
input unchanged, while `Path.expanduser` raises `RuntimeError`.

Additionally, the fix is marked as unsafe because `os.path.expanduser()` returns `str` or `bytes` (`AnyStr`),
while `Path.expanduser()` returns a `Path` object. This change in return type can break code that uses
the return value.

## [References](#references)

* [Python documentation: `Path.expanduser`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser)
* [Python documentation: `os.path.expanduser`](https://docs.python.org/3/library/os.path.html#os.path.expanduser)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)