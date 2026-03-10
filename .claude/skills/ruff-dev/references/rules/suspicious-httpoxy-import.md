# [suspicious-httpoxy-import (S412)](#suspicious-httpoxy-import-s412)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-httpoxy-import%27%20OR%20S412)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L302)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of `wsgiref.handlers.CGIHandler` and
`twisted.web.twcgi.CGIScript`.

## [Why is this bad?](#why-is-this-bad)

httpoxy is a set of vulnerabilities that affect application code running in
CGI or CGI-like environments. The use of CGI for web applications should be
avoided to prevent this class of attack.

## [Example](#example)

```
from wsgiref.handlers import CGIHandler
```

## [References](#references)

* [httpoxy website](https://httpoxy.org/)