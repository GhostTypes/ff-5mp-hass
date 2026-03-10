# [hardcoded-password-func-arg (S106)](#hardcoded-password-func-arg-s106)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-password-func-arg%27%20OR%20S106)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fhardcoded_password_func_arg.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for potential uses of hardcoded passwords in function calls.

## [Why is this bad?](#why-is-this-bad)

Including a hardcoded password in source code is a security risk, as an
attacker could discover the password and use it to gain unauthorized
access.

Instead, store passwords and other secrets in configuration files,
environment variables, or other sources that are excluded from version
control.

## [Example](#example)

```
connect_to_server(password="hunter2")
```

Use instead:

```
import os

connect_to_server(password=os.environ["PASSWORD"])
```

## [References](#references)

* [Common Weakness Enumeration: CWE-259](https://cwe.mitre.org/data/definitions/259.html)