# [shebang-not-executable (EXE001)](#shebang-not-executable-exe001)

Added in [v0.0.233](https://github.com/astral-sh/ruff/releases/tag/v0.0.233) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27shebang-not-executable%27%20OR%20EXE001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_executable%2Frules%2Fshebang_not_executable.rs#L40)

Derived from the **[flake8-executable](../#flake8-executable-exe)** linter.

## [What it does](#what-it-does)

Checks for a shebang directive in a file that is not executable.

## [Why is this bad?](#why-is-this-bad)

In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.

The presence of a shebang suggests that a file is intended to be
executable. If a file contains a shebang but is not executable, then the
shebang is misleading, or the file is missing the executable bit.

If the file is meant to be executable, add the executable bit to the file
(e.g., `chmod +x __main__.py` or `git update-index --chmod=+x __main__.py`).

Otherwise, remove the shebang.

A file is considered executable if it has the executable bit set (i.e., its
permissions mode intersects with `0o111`). As such, *this rule is only
available on Unix-like systems*, and is not enforced on Windows or WSL.

## [Example](#example)

```
#!/usr/bin/env python
```

## [References](#references)

* [Python documentation: Executable Python Scripts](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)
* [Git documentation: `git update-index --chmod`](https://git-scm.com/docs/git-update-index#Documentation/git-update-index.txt---chmod-x)