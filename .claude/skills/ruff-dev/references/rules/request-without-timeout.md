# [request-without-timeout (S113)](#request-without-timeout-s113)

Added in [v0.0.213](https://github.com/astral-sh/ruff/releases/tag/v0.0.213) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27request-without-timeout%27%20OR%20S113)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Frequest_without_timeout.rs#L35)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the Python `requests` or `httpx` module that omit the
`timeout` parameter.

## [Why is this bad?](#why-is-this-bad)

The `timeout` parameter is used to set the maximum time to wait for a
response from the server. By omitting the `timeout` parameter, the program
may hang indefinitely while awaiting a response.

## [Example](#example)

```
import requests

requests.get("https://www.example.com/")
```

Use instead:

```
import requests

requests.get("https://www.example.com/", timeout=10)
```

## [References](#references)

* [Requests documentation: Timeouts](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts)
* [httpx documentation: Timeouts](https://www.python-httpx.org/advanced/timeouts/)