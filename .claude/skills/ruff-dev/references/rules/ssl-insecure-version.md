# [ssl-insecure-version (S502)](#ssl-insecure-version-s502)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ssl-insecure-version%27%20OR%20S502)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fssl_insecure_version.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for function calls with parameters that indicate the use of insecure
SSL and TLS protocol versions.

## [Why is this bad?](#why-is-this-bad)

Several highly publicized exploitable flaws have been discovered in all
versions of SSL and early versions of TLS. The following versions are
considered insecure, and should be avoided:

* SSL v2
* SSL v3
* TLS v1
* TLS v1.1

This method supports detection on the Python's built-in `ssl` module and
the `pyOpenSSL` module.

## [Example](#example)

```
import ssl

ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1)
```

Use instead:

```
import ssl

ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1_2)
```