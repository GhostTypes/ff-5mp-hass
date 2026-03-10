# [suspicious-mktemp-usage (S306)](#suspicious-mktemp-usage-s306)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-mktemp-usage%27%20OR%20S306)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L297)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of `tempfile.mktemp`.

## [Why is this bad?](#why-is-this-bad)

`tempfile.mktemp` returns a pathname of a file that does not exist at the
time the call is made; then, the caller is responsible for creating the
file and subsequently using it. This is insecure because another process
could create a file with the same name between the time the function
returns and the time the caller creates the file.

`tempfile.mktemp` is deprecated in favor of `tempfile.mkstemp` which
creates the file when it is called. Consider using `tempfile.mkstemp`
instead, either directly or via a context manager such as
`tempfile.TemporaryFile`.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to `tempfile.mktemp`.

## [Example](#example)

```
import tempfile

tmp_file = tempfile.mktemp()
with open(tmp_file, "w") as file:
    file.write("Hello, world!")
```

Use instead:

```
import tempfile

with tempfile.TemporaryFile() as file:
    file.write("Hello, world!")
```

## [References](#references)

* [Python documentation:`mktemp`](https://docs.python.org/3/library/tempfile.html#tempfile.mktemp)