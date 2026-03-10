# [replace-universal-newlines (UP021)](#replace-universal-newlines-up021)

Added in [v0.0.196](https://github.com/astral-sh/ruff/releases/tag/v0.0.196) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27replace-universal-newlines%27%20OR%20UP021)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Freplace_universal_newlines.rs#L37)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `subprocess.run` that set the `universal_newlines`
keyword argument.

## [Why is this bad?](#why-is-this-bad)

As of Python 3.7, the `universal_newlines` keyword argument has been
renamed to `text`, and now exists for backwards compatibility. The
`universal_newlines` keyword argument may be removed in a future version of
Python. Prefer `text`, which is more explicit and readable.

## [Example](#example)

```
import subprocess

subprocess.run(["foo"], universal_newlines=True)
```

Use instead:

```
import subprocess

subprocess.run(["foo"], text=True)
```

## [References](#references)

* [Python 3.7 release notes](https://docs.python.org/3/whatsnew/3.7.html#subprocess)
* [Python documentation: `subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run)