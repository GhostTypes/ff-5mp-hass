# [suspicious-xmle-tree-usage (S320)](#suspicious-xmle-tree-usage-s320)

Removed (since [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-xmle-tree-usage%27%20OR%20S320)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L845)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule was removed as the `lxml` library has been modified to address
known vulnerabilities and unsafe defaults. As such, the `defusedxml`
library is no longer necessary, `defusedxml` has [deprecated](https://pypi.org/project/defusedxml/0.8.0rc2/#defusedxml-lxml) its `lxml`
module.

## [What it does](#what-it-does)

Checks for uses of insecure XML parsers.

## [Why is this bad?](#why-is-this-bad)

Many XML parsers are vulnerable to XML attacks (such as entity expansion),
which cause excessive memory and CPU usage by exploiting recursion. An
attacker could use such methods to access unauthorized resources.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to insecure XML parsers.

## [Example](#example)

```
from lxml import etree

content = etree.parse("untrusted.xml")
```

## [References](#references)

* [PyPI: `lxml`](https://pypi.org/project/lxml/)
* [Common Weakness Enumeration: CWE-400](https://cwe.mitre.org/data/definitions/400.html)
* [Common Weakness Enumeration: CWE-776](https://cwe.mitre.org/data/definitions/776.html)