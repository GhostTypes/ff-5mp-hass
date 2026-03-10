# [snmp-weak-cryptography (S509)](#snmp-weak-cryptography-s509)

Added in [v0.0.218](https://github.com/astral-sh/ruff/releases/tag/v0.0.218) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27snmp-weak-cryptography%27%20OR%20S509)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsnmp_weak_cryptography.rs#L32)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the SNMPv3 protocol without encryption.

## [Why is this bad?](#why-is-this-bad)

Unencrypted SNMPv3 communication can be intercepted and read by
unauthorized parties. Instead, enable encryption when using SNMPv3.

## [Example](#example)

```
from pysnmp.hlapi import UsmUserData

UsmUserData("user")
```

Use instead:

```
from pysnmp.hlapi import UsmUserData

UsmUserData("user", "authkey", "privkey")
```

## [References](#references)

* [Common Weakness Enumeration: CWE-319](https://cwe.mitre.org/data/definitions/319.html)