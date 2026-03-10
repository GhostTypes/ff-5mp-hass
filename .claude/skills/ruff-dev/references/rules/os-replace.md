# [os-replace (PTH105)](#os-replace-pth105)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-replace%27%20OR%20PTH105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_replace.rs#L56)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `os.replace`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os`. When possible, using `Path` object
methods such as `Path.replace()` can improve readability over the `os`
module's counterparts (e.g., `os.replace()`).

Note that `os` functions may be preferable if performance is a concern,
e.g., in hot loops.

## [Examples](#examples)

```
import os

os.replace("old.py", "new.py")
```

Use instead:

```
from pathlib import Path

Path("old.py").replace("new.py")
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.
Additionally, the fix is marked as unsafe when the return value is used because the type changes
from `None` to a `Path` object.

## [References](#references)

* [Python documentation: `Path.replace`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace)
* [Python documentation: `os.replace`](https://docs.python.org/3/library/os.html#os.replace)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)