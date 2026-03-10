# [open-file-with-context-handler (SIM115)](#open-file-with-context-handler-sim115)

Added in [v0.0.219](https://github.com/astral-sh/ruff/releases/tag/v0.0.219) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27open-file-with-context-handler%27%20OR%20SIM115)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_simplify%2Frules%2Fopen_file_with_context_handler.rs#L36)

Derived from the **[flake8-simplify](../#flake8-simplify-sim)** linter.

## [What it does](#what-it-does)

Checks for cases where files are opened (e.g., using the builtin `open()` function)
without using a context manager.

## [Why is this bad?](#why-is-this-bad)

If a file is opened without a context manager, it is not guaranteed that
the file will be closed (e.g., if an exception is raised), which can cause
resource leaks. The rule detects a wide array of IO calls where context managers
could be used, such as `open`, `pathlib.Path(...).open()`, `tempfile.TemporaryFile()`
or`tarfile.TarFile(...).gzopen()`.

## [Example](#example)

```
file = open("foo.txt")
...
file.close()
```

Use instead:

```
with open("foo.txt") as file:
    ...
```

## [References](#references)

* [Python documentation: `open`](https://docs.python.org/3/library/functions.html#open)