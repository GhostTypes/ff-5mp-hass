# [suspicious-telnet-usage (S312)](#suspicious-telnet-usage-s312)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-telnet-usage%27%20OR%20S312)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L918)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for the use of Telnet-related functions.

## [Why is this bad?](#why-is-this-bad)

Telnet is considered insecure because it does not encrypt data sent over
the connection and is vulnerable to numerous attacks.

Instead, consider using a more secure protocol such as SSH.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to Telnet-related functions.

## [References](#references)

* [Python documentation: `telnetlib` — Telnet client](https://docs.python.org/3/library/telnetlib.html)