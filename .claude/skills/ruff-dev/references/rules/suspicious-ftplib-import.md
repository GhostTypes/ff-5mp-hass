# [suspicious-ftplib-import (S402)](#suspicious-ftplib-import-s402)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-ftplib-import%27%20OR%20S402)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L52)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `ftplib` module.

## [Why is this bad?](#why-is-this-bad)

FTP is considered insecure. Instead, use SSH, SFTP, SCP, or another
encrypted protocol.

## [Example](#example)

```
import ftplib
```

## [References](#references)

* [Python documentation: `ftplib` - FTP protocol client](https://docs.python.org/3/library/ftplib.html)