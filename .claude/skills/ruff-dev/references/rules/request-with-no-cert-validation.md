# [request-with-no-cert-validation (S501)](#request-with-no-cert-validation-s501)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27request-with-no-cert-validation%27%20OR%20S501)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Frequest_with_no_cert_validation.rs#L33)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for HTTPS requests that disable SSL certificate checks.

## [Why is this bad?](#why-is-this-bad)

If SSL certificates are not verified, an attacker could perform a "man in
the middle" attack by intercepting and modifying traffic between the client
and server.

## [Example](#example)

```
import requests

requests.get("https://www.example.com", verify=False)
```

Use instead:

```
import requests

requests.get("https://www.example.com")  # By default, `verify=True`.
```

## [References](#references)

* [Common Weakness Enumeration: CWE-295](https://cwe.mitre.org/data/definitions/295.html)