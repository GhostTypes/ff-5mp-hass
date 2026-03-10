# [ssl-with-no-version (S504)](#ssl-with-no-version-s504)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ssl-with-no-version%27%20OR%20S504)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fssl_with_no_version.rs#L28)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for calls to `ssl.wrap_socket()` without an `ssl_version`.

## [Why is this bad?](#why-is-this-bad)

This method is known to provide a default value that maximizes
compatibility, but permits use of insecure protocols.

## [Example](#example)

```
import ssl

ssl.wrap_socket()
```

Use instead:

```
import ssl

ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2)
```