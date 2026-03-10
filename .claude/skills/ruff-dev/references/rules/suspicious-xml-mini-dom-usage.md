# [suspicious-xml-mini-dom-usage (S318)](#suspicious-xml-mini-dom-usage-s318)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-xml-mini-dom-usage%27%20OR%20S318)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L758)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of insecure XML parsers.

## [Why is this bad?](#why-is-this-bad)

Many XML parsers are vulnerable to XML attacks (such as entity expansion),
which cause excessive memory and CPU usage by exploiting recursion. An
attacker could use such methods to access unauthorized resources.

Consider using the `defusedxml` package when parsing untrusted XML data,
to protect against XML attacks.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to insecure XML parsers.

## [Example](#example)

```
from xml.dom.minidom import parse

content = parse("untrusted.xml")
```

Use instead:

```
from defusedxml.minidom import parse

content = parse("untrusted.xml")
```

## [References](#references)

* [Python documentation: `xml` — XML processing modules](https://docs.python.org/3/library/xml.html)
* [PyPI: `defusedxml`](https://pypi.org/project/defusedxml/)
* [Common Weakness Enumeration: CWE-400](https://cwe.mitre.org/data/definitions/400.html)
* [Common Weakness Enumeration: CWE-776](https://cwe.mitre.org/data/definitions/776.html)