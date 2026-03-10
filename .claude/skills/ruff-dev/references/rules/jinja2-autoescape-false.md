# [jinja2-autoescape-false (S701)](#jinja2-autoescape-false-s701)

Added in [v0.0.220](https://github.com/astral-sh/ruff/releases/tag/v0.0.220) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27jinja2-autoescape-false%27%20OR%20S701)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fjinja2_autoescape_false.rs#L37)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for `jinja2` templates that use `autoescape=False`.

## [Why is this bad?](#why-is-this-bad)

`jinja2` templates that use `autoescape=False` are vulnerable to cross-site
scripting (XSS) attacks that allow attackers to execute arbitrary
JavaScript.

By default, `jinja2` sets `autoescape` to `False`, so it is important to
set `autoescape=True` or use the `select_autoescape` function to mitigate
XSS vulnerabilities.

## [Example](#example)

```
import jinja2

jinja2.Environment(loader=jinja2.FileSystemLoader("."))
```

Use instead:

```
import jinja2

jinja2.Environment(loader=jinja2.FileSystemLoader("."), autoescape=True)
```

## [References](#references)

* [Jinja documentation: API](https://jinja.palletsprojects.com/en/latest/api/#autoescaping)
* [Common Weakness Enumeration: CWE-94](https://cwe.mitre.org/data/definitions/94.html)