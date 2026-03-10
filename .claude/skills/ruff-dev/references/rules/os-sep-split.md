# [os-sep-split (PTH206)](#os-sep-split-pth206)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-sep-split%27%20OR%20PTH206)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fos_sep_split.rs#L55)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

## [What it does](#what-it-does)

Checks for uses of `.split(os.sep)`

## [Why is this bad?](#why-is-this-bad)

The `pathlib` module in the standard library should be used for path
manipulation. It provides a high-level API with the functionality
needed for common operations on `Path` objects.

## [Example](#example)

If not all parts of the path are needed, then the `name` and `parent`
attributes of the `Path` object should be used. Otherwise, the `parts`
attribute can be used as shown in the last example.

```
import os

"path/to/file_name.txt".split(os.sep)[-1]

"path/to/file_name.txt".split(os.sep)[-2]

# Iterating over the path parts
if any(part in blocklist for part in "my/file/path".split(os.sep)):
    ...
```

Use instead:

```
from pathlib import Path

Path("path/to/file_name.txt").name

Path("path/to/file_name.txt").parent.name

# Iterating over the path parts
if any(part in blocklist for part in Path("my/file/path").parts):
    ...
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than working directly with strings,
especially on older versions of Python.

## [References](#references)

* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)