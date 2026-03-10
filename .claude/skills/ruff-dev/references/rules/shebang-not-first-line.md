# [shebang-not-first-line (EXE005)](#shebang-not-first-line-exe005)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27shebang-not-first-line%27%20OR%20EXE005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_executable%2Frules%2Fshebang_not_first_line.rs#L35)

Derived from the **[flake8-executable](../#flake8-executable-exe)** linter.

## [What it does](#what-it-does)

Checks for a shebang directive that is not at the beginning of the file.

## [Why is this bad?](#why-is-this-bad)

In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.

The shebang's `#!` prefix must be the first two characters of a file. If
the shebang is not at the beginning of the file, it will be ignored, which
is likely a mistake.

## [Example](#example)

```
foo = 1
#!/usr/bin/env python3
```

Use instead:

```
#!/usr/bin/env python3
foo = 1
```

## [References](#references)

* [Python documentation: Executable Python Scripts](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)