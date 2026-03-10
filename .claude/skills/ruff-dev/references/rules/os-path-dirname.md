# [os-path-dirname (PTH120)](#os-path-dirname-pth120)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-path-dirname%27%20OR%20PTH120)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_path_dirname.rs#L61)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.path.dirname`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os.path`. When possible, using `Path` object
methods such as `Path.parent` can improve readability over the `os.path`
module's counterparts (e.g., `os.path.dirname()`).

## [Examples](#examples)

```
import os

os.path.dirname(__file__)
```

Use instead:

```
from pathlib import Path

Path(__file__).parent
```

## [Fix Safety](#fix-safety)

This rule's fix is always marked as unsafe because the replacement is not always semantically
equivalent to the original code. In particular, `pathlib` performs path normalization,
which can alter the result compared to `os.path.dirname`. For example, this normalization:

* Collapses consecutive slashes (e.g., `"a//b"` → `"a/b"`).
* Removes trailing slashes (e.g., `"a/b/"` → `"a/b"`).
* Eliminates `"."` (e.g., `"a/./b"` → `"a/b"`).

As a result, code relying on the exact string returned by `os.path.dirname`
may behave differently after the fix.

Additionally, the fix is marked as unsafe because `os.path.dirname()` returns `str` or `bytes` (`AnyStr`),
while `Path.parent` returns a `Path` object. This change in return type can break code that uses
the return value.

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [References](#references)

* [Python documentation: `PurePath.parent`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent)
* [Python documentation: `os.path.dirname`](https://docs.python.org/3/library/os.path.html#os.path.dirname)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)