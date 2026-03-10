# [mako-templates (S702)](#mako-templates-s702)

Added in [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27mako-templates%27%20OR%20S702)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fmako_templates.rs#L35)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the `mako` templates.

## [Why is this bad?](#why-is-this-bad)

Mako templates allow HTML and JavaScript rendering by default, and are
inherently open to XSS attacks. Ensure variables in all templates are
properly sanitized via the `n`, `h` or `x` flags (depending on context).
For example, to HTML escape the variable `data`, use `${ data |h }`.

## [Example](#example)

```
from mako.template import Template

Template("hello")
```

Use instead:

```
from mako.template import Template

Template("hello |h")
```

## [References](#references)

* [Mako documentation](https://www.makotemplates.org/)
* [OpenStack security: Cross site scripting XSS](https://security.openstack.org/guidelines/dg_cross-site-scripting-xss.html)
* [Common Weakness Enumeration: CWE-80](https://cwe.mitre.org/data/definitions/80.html)