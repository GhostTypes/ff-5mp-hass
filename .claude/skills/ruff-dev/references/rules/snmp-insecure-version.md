# [snmp-insecure-version (S508)](#snmp-insecure-version-s508)

Added in [v0.0.218](https://github.com/astral-sh/ruff/releases/tag/v0.0.218) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27snmp-insecure-version%27%20OR%20S508)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsnmp_insecure_version.rs#L34)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of SNMPv1 or SNMPv2.

## [Why is this bad?](#why-is-this-bad)

The SNMPv1 and SNMPv2 protocols are considered insecure as they do
not support encryption. Instead, prefer SNMPv3, which supports
encryption.

## [Example](#example)

```
from pysnmp.hlapi import CommunityData

CommunityData("public", mpModel=0)
```

Use instead:

```
from pysnmp.hlapi import CommunityData

CommunityData("public", mpModel=2)
```

## [References](#references)

* [Cybersecurity and Infrastructure Security Agency (CISA): Alert TA17-156A](https://www.cisa.gov/news-events/alerts/2017/06/05/reducing-risk-snmp-abuse)
* [Common Weakness Enumeration: CWE-319](https://cwe.mitre.org/data/definitions/319.html)