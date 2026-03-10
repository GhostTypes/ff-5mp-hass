# [assignment-to-os-environ (B003)](#assignment-to-os-environ-b003)

Added in [v0.0.102](https://github.com/astral-sh/ruff/releases/tag/v0.0.102) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assignment-to-os-environ%27%20OR%20B003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fassignment_to_os_environ.rs#L42)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for assignments to `os.environ`.

## [Why is this bad?](#why-is-this-bad)

In Python, `os.environ` is a mapping that represents the environment of the
current process.

However, reassigning to `os.environ` does not clear the environment. Instead,
it merely updates the `os.environ` for the current process. This can lead to
unexpected behavior, especially when running the program in a subprocess.

Instead, use `os.environ.clear()` to clear the environment, or use the
`env` argument of `subprocess.Popen` to pass a custom environment to
a subprocess.

## [Example](#example)

```
import os

os.environ = {"foo": "bar"}
```

Use instead:

```
import os

os.environ.clear()
os.environ["foo"] = "bar"
```

## [References](#references)

* [Python documentation: `os.environ`](https://docs.python.org/3/library/os.html#os.environ)
* [Python documentation: `subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen)