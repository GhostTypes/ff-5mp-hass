# [shebang-missing-python (EXE003)](#shebang-missing-python-exe003)

Added in [v0.0.229](https://github.com/astral-sh/ruff/releases/tag/v0.0.229) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27shebang-missing-python%27%20OR%20EXE003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_executable%2Frules%2Fshebang_missing_python.rs#L34)

Derived from the **[flake8-executable](../#flake8-executable-exe)** linter.

## [What it does](#what-it-does)

Checks for a shebang directive in `.py` files that does not contain `python`,
`pytest`, or `uv run`.

## [Why is this bad?](#why-is-this-bad)

In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the command that should be used to run the
script.

For Python scripts, if the shebang does not include a command that explicitly
or implicitly specifies an interpreter, then the file will be executed with
the default interpreter, which is likely a mistake.

## [Example](#example)

```
#!/usr/bin/env bash
```

Use instead:

```
#!/usr/bin/env python3
```

## [References](#references)

* [Python documentation: Executable Python Scripts](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)