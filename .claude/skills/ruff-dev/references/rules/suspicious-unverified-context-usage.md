# [suspicious-unverified-context-usage (S323)](#suspicious-unverified-context-usage-s323)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-unverified-context-usage%27%20OR%20S323)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L892)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of `ssl._create_unverified_context`.

## [Why is this bad?](#why-is-this-bad)

[PEP 476](https://peps.python.org/pep-0476/) enabled certificate and hostname validation by default in Python
standard library HTTP clients. Previously, Python did not validate
certificates by default, which could allow an attacker to perform a "man in
the middle" attack by intercepting and modifying traffic between client and
server.

To support legacy environments, `ssl._create_unverified_context` reverts to
the previous behavior that does perform verification. Otherwise, use
`ssl.create_default_context` to create a secure context.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to `ssl._create_unverified_context`.

## [Example](#example)

```
import ssl

context = ssl._create_unverified_context()
```

Use instead:

```
import ssl

context = ssl.create_default_context()
```

## [References](#references)

* [PEP 476 – Enabling certificate verification by default for stdlib http clients: Opting out](https://peps.python.org/pep-0476/#opting-out)
* [Python documentation: `ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)