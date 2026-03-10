# [hardcoded-bind-all-interfaces (S104)](#hardcoded-bind-all-interfaces-s104)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27hardcoded-bind-all-interfaces%27%20OR%20S104)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fhardcoded_bind_all_interfaces.rs#L29)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for hardcoded bindings to all network interfaces (`0.0.0.0`).

## [Why is this bad?](#why-is-this-bad)

Binding to all network interfaces is insecure as it allows access from
unintended interfaces, which may be poorly secured or unauthorized.

Instead, bind to specific interfaces.

## [Example](#example)

```
ALLOWED_HOSTS = ["0.0.0.0"]
```

Use instead:

```
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```

## [References](#references)

* [Common Weakness Enumeration: CWE-200](https://cwe.mitre.org/data/definitions/200.html)