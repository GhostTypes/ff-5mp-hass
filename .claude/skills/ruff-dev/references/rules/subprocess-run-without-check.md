# [subprocess-run-without-check (PLW1510)](#subprocess-run-without-check-plw1510)

Added in [v0.0.285](https://github.com/astral-sh/ruff/releases/tag/v0.0.285) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27subprocess-run-without-check%27%20OR%20PLW1510)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsubprocess_run_without_check.rs#L48)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `subprocess.run` without an explicit `check` argument.

## [Why is this bad?](#why-is-this-bad)

By default, `subprocess.run` does not check the return code of the process
it runs. This can lead to silent failures.

Instead, consider using `check=True` to raise an exception if the process
fails, or set `check=False` explicitly to mark the behavior as intentional.

## [Example](#example)

```
import subprocess

subprocess.run(["ls", "nonexistent"])  # No exception raised.
```

Use instead:

```
import subprocess

subprocess.run(["ls", "nonexistent"], check=True)  # Raises exception.
```

Or:

```
import subprocess

subprocess.run(["ls", "nonexistent"], check=False)  # Explicitly no check.
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe for function calls that contain
`**kwargs`, as adding a `check` keyword argument to such a call may lead
to a duplicate keyword argument error.

## [References](#references)

* [Python documentation: `subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run)