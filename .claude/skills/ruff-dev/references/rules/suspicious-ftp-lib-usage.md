# [suspicious-ftp-lib-usage (S321)](#suspicious-ftp-lib-usage-s321)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-ftp-lib-usage%27%20OR%20S321)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L944)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for the use of FTP-related functions.

## [Why is this bad?](#why-is-this-bad)

FTP is considered insecure as it does not encrypt data sent over the
connection and is thus vulnerable to numerous attacks.

Instead, consider using FTPS (which secures FTP using SSL/TLS) or SFTP.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to FTP-related functions.

## [References](#references)

* [Python documentation: `ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html)