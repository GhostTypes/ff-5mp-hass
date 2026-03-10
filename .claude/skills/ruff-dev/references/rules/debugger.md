# [debugger (T100)](#debugger-t100)

Added in [v0.0.141](https://github.com/astral-sh/ruff/releases/tag/v0.0.141) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27debugger%27%20OR%20T100)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_debugger%2Frules%2Fdebugger.rs#L33)

Derived from the **[flake8-debugger](../#flake8-debugger-t10)** linter.

## [What it does](#what-it-does)

Checks for the presence of debugger calls and imports.

## [Why is this bad?](#why-is-this-bad)

Debugger calls and imports should be used for debugging purposes only. The
presence of a debugger call or import in production code is likely a
mistake and may cause unintended behavior, such as exposing sensitive
information or causing the program to hang.

Instead, consider using a logging library to log information about the
program's state, and writing tests to verify that the program behaves
as expected.

## [Example](#example)

```
def foo():
    breakpoint()
```

## [References](#references)

* [Python documentation: `pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
* [Python documentation: `logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html)