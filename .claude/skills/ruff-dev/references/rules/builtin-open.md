# [builtin-open (PTH123)](#builtin-open-pth123)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27builtin-open%27%20OR%20PTH123)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Frules%2Fbuiltin_open.rs#L52)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of the `open()` builtin.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation. When possible,
using `Path` object methods such as `Path.open()` can improve readability
over the `open` builtin.

## [Examples](#examples)

```
with open("f1.py", "wb") as fp:
    ...
```

Use instead:

```
from pathlib import Path

with Path("f1.py").open("wb") as fp:
    ...
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than working directly with strings,
especially on older versions of Python.

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if the replacement would remove comments attached to the original expression.

## [References](#references)

* [Python documentation: `Path.open`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open)
* [Python documentation: `open`](https://docs.python.org/3/library/functions.html#open)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)