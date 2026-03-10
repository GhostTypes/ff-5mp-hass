# [replace-stdout-stderr (UP022)](#replace-stdout-stderr-up022)

Added in [v0.0.199](https://github.com/astral-sh/ruff/releases/tag/v0.0.199) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27replace-stdout-stderr%27%20OR%20UP022)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Freplace_stdout_stderr.rs#L45)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for uses of `subprocess.run` that send `stdout` and `stderr` to a
pipe.

## [Why is this bad?](#why-is-this-bad)

As of Python 3.7, `subprocess.run` has a `capture_output` keyword argument
that can be set to `True` to capture `stdout` and `stderr` outputs. This is
equivalent to setting `stdout` and `stderr` to `subprocess.PIPE`, but is
more explicit and readable.

## [Example](#example)

```
import subprocess

subprocess.run(["foo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```

Use instead:

```
import subprocess

subprocess.run(["foo"], capture_output=True)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because replacing `stdout=subprocess.PIPE` and
`stderr=subprocess.PIPE` with `capture_output=True` may delete comments attached
to the original arguments.

## [References](#references)

* [Python 3.7 release notes](https://docs.python.org/3/whatsnew/3.7.html#subprocess)
* [Python documentation: `subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run)