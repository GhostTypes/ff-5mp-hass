# [suspicious-telnetlib-import (S401)](#suspicious-telnetlib-import-s401)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-telnetlib-import%27%20OR%20S401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L27)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `telnetlib` module.

## [Why is this bad?](#why-is-this-bad)

Telnet is considered insecure. It is deprecated since version 3.11, and
was removed in version 3.13. Instead, use SSH or another encrypted
protocol.

## [Example](#example)

```
import telnetlib
```

## [References](#references)

* [Python documentation: `telnetlib` - Telnet client](https://docs.python.org/3.12/library/telnetlib.html#module-telnetlib)
* [PEP 594: `telnetlib`](https://peps.python.org/pep-0594/#telnetlib)