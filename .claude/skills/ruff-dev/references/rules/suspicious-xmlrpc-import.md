# [suspicious-xmlrpc-import (S411)](#suspicious-xmlrpc-import-s411)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-xmlrpc-import%27%20OR%20S411)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L275)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `xmlrpc` module.

## [Why is this bad?](#why-is-this-bad)

XMLRPC is a particularly dangerous XML module, as it is also concerned with
communicating data over a network. Use the `defused.xmlrpc.monkey_patch()`
function to monkey-patch the `xmlrpclib` module and mitigate remote XML
attacks.

## [Example](#example)

```
import xmlrpc
```