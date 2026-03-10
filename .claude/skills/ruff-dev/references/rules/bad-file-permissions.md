# [bad-file-permissions (S103)](#bad-file-permissions-s103)

Added in [v0.0.211](https://github.com/astral-sh/ruff/releases/tag/v0.0.211) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-file-permissions%27%20OR%20S103)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fbad_file_permissions.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for files with overly permissive permissions.

## [Why is this bad?](#why-is-this-bad)

Overly permissive file permissions may allow unintended access and
arbitrary code execution.

## [Example](#example)

```
import os

os.chmod("/etc/secrets.txt", 0o666)  # rw-rw-rw-
```

Use instead:

```
import os

os.chmod("/etc/secrets.txt", 0o600)  # rw-------
```

## [References](#references)

* [Python documentation: `os.chmod`](https://docs.python.org/3/library/os.html#os.chmod)
* [Python documentation: `stat`](https://docs.python.org/3/library/stat.html)
* [Common Weakness Enumeration: CWE-732](https://cwe.mitre.org/data/definitions/732.html)