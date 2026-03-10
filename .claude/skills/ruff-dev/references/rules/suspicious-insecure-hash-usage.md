# [suspicious-insecure-hash-usage (S303)](#suspicious-insecure-hash-usage-s303)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-insecure-hash-usage%27%20OR%20S303)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L159)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of weak or broken cryptographic hash functions.

## [Why is this bad?](#why-is-this-bad)

Weak or broken cryptographic hash functions may be susceptible to
collision attacks (where two different inputs produce the same hash) or
pre-image attacks (where an attacker can find an input that produces a
given hash). This can lead to security vulnerabilities in applications
that rely on these hash functions.

Avoid using weak or broken cryptographic hash functions in security
contexts. Instead, use a known secure hash function such as SHA-256.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to insecure hash functions.

## [Example](#example)

```
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.MD5())
digest.update(b"Hello, world!")
digest.finalize()
```

Use instead:

```
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"Hello, world!")
digest.finalize()
```

## [References](#references)

* [Python documentation: `hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
* [Common Weakness Enumeration: CWE-327](https://cwe.mitre.org/data/definitions/327.html)
* [Common Weakness Enumeration: CWE-328](https://cwe.mitre.org/data/definitions/328.html)
* [Common Weakness Enumeration: CWE-916](https://cwe.mitre.org/data/definitions/916.html)