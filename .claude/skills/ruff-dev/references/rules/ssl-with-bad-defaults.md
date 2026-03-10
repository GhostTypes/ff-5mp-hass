# [ssl-with-bad-defaults (S503)](#ssl-with-bad-defaults-s503)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ssl-with-bad-defaults%27%20OR%20S503)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fssl_with_bad_defaults.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for function definitions with default arguments set to insecure SSL
and TLS protocol versions.

## [Why is this bad?](#why-is-this-bad)

Several highly publicized exploitable flaws have been discovered in all
versions of SSL and early versions of TLS. The following versions are
considered insecure, and should be avoided:

* SSL v2
* SSL v3
* TLS v1
* TLS v1.1

## [Example](#example)

```
import ssl


def func(version=ssl.PROTOCOL_TLSv1): ...
```

Use instead:

```
import ssl


def func(version=ssl.PROTOCOL_TLSv1_2): ...
```