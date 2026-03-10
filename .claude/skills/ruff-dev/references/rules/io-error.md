# [io-error (E902)](#io-error-e902)

Added in [v0.0.28](https://github.com/astral-sh/ruff/releases/tag/v0.0.28) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27io-error%27%20OR%20E902)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Ferrors.rs#L27)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

This is not a regular diagnostic; instead, it's raised when a file cannot be read
from disk.

## [Why is this bad?](#why-is-this-bad)

An `IOError` indicates an error in the development setup. For example, the user may
not have permissions to read a given file, or the filesystem may contain a broken
symlink.

## [Example](#example)

On Linux or macOS:

```
$ echo 'print("hello world!")' > a.py
$ chmod 000 a.py
$ ruff a.py
a.py:1:1: E902 Permission denied (os error 13)
Found 1 error.
```

## [References](#references)

* [UNIX Permissions introduction](https://mason.gmu.edu/~montecin/UNIXpermiss.htm)
* [Command Line Basics: Symbolic Links](https://www.digitalocean.com/community/tutorials/workflow-symbolic-links)