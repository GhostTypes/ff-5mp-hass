# [hardcoded-password-string (S105)](#hardcoded-password-string-s105)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-password-string%27%20OR%20S105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fhardcoded_password_string.rs#L36)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for potential uses of hardcoded passwords in strings.

## [Why is this bad?](#why-is-this-bad)

Including a hardcoded password in source code is a security risk, as an
attacker could discover the password and use it to gain unauthorized
access.

Instead, store passwords and other secrets in configuration files,
environment variables, or other sources that are excluded from version
control.

## [Example](#example)

```
SECRET_KEY = "hunter2"
```

Use instead:

```
import os

SECRET_KEY = os.environ["SECRET_KEY"]
```

## [References](#references)

* [Common Weakness Enumeration: CWE-259](https://cwe.mitre.org/data/definitions/259.html)