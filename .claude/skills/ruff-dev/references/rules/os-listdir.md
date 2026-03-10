# [os-listdir (PTH208)](#os-listdir-pth208)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27os-listdir%27%20OR%20PTH208)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_use_pathlib%2Fviolations.rs#L264)

Derived from the **[flake8-use-pathlib](../#flake8-use-pathlib-pth)** linter.

## [What it does](#what-it-does)

Checks for uses of `os.listdir`.

## [Why is this bad?](#why-is-this-bad)

`pathlib` offers a high-level API for path manipulation, as compared to
the lower-level API offered by `os`. When possible, using `pathlib`'s
`Path.iterdir()` can improve readability over `os.listdir()`.

## [Example](#example)

```
p = "."
for d in os.listdir(p):
    ...

if os.listdir(p):
    ...

if "file" in os.listdir(p):
    ...
```

Use instead:

```
p = Path(".")
for d in p.iterdir():
    ...

if any(p.iterdir()):
    ...

if (p / "file").exists():
    ...
```

## [Known issues](#known-issues)

While using `pathlib` can improve the readability and type safety of your code,
it can be less performant than the lower-level alternatives that work directly with strings,
especially on older versions of Python.

## [References](#references)

* [Python documentation: `Path.iterdir`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.iterdir)
* [Python documentation: `os.listdir`](https://docs.python.org/3/library/os.html#os.listdir)
* [PEP 428 – The pathlib module – object-oriented filesystem paths](https://peps.python.org/pep-0428/)
* [Correspondence between `os` and `pathlib`](https://docs.python.org/3/library/pathlib.html#corresponding-tools)
* [Why you should be using pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)
* [No really, pathlib is great](https://treyhunner.com/2019/01/no-really-pathlib-is-great/)