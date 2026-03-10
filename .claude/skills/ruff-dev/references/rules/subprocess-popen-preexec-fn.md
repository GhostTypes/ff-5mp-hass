# [subprocess-popen-preexec-fn (PLW1509)](#subprocess-popen-preexec-fn-plw1509)

Added in [v0.0.281](https://github.com/astral-sh/ruff/releases/tag/v0.0.281) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27subprocess-popen-preexec-fn%27%20OR%20PLW1509)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsubprocess_popen_preexec_fn.rs#L42)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of `subprocess.Popen` with a `preexec_fn` argument.

## [Why is this bad?](#why-is-this-bad)

The `preexec_fn` argument is unsafe within threads as it can lead to
deadlocks. Furthermore, `preexec_fn` is [targeted for deprecation](https://github.com/python/cpython/issues/82616).

Instead, consider using task-specific arguments such as `env`,
`start_new_session`, and `process_group`. These are not prone to deadlocks
and are more explicit.

## [Example](#example)

```
import os, subprocess

subprocess.Popen(foo, preexec_fn=os.setsid)
subprocess.Popen(bar, preexec_fn=os.setpgid(0, 0))
```

Use instead:

```
import subprocess

subprocess.Popen(foo, start_new_session=True)
subprocess.Popen(bar, process_group=0)  # Introduced in Python 3.11
```

## [References](#references)

* [Python documentation: `subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#popen-constructor)
* [Why `preexec_fn` in `subprocess.Popen` may lead to deadlock?](https://discuss.python.org/t/why-preexec-fn-in-subprocess-popen-may-lead-to-deadlock/16908/2)