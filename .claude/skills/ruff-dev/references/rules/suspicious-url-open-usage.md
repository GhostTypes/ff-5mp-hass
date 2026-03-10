# [suspicious-url-open-usage (S310)](#suspicious-url-open-usage-s310)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-url-open-usage%27%20OR%20S310)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L445)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for instances where URL open functions are used with unexpected schemes.

## [Why is this bad?](#why-is-this-bad)

Some URL open functions allow the use of `file:` or custom schemes (for use
instead of `http:` or `https:`). An attacker may be able to use these
schemes to access or modify unauthorized resources, and cause unexpected
behavior.

To mitigate this risk, audit all uses of URL open functions and ensure that
only permitted schemes are used (e.g., allowing `http:` and `https:`, and
disallowing `file:` and `ftp:`).

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to URL open functions.

## [Example](#example)

```
from urllib.request import urlopen

url = input("Enter a URL: ")

with urlopen(url) as response:
    ...
```

Use instead:

```
from urllib.request import urlopen

url = input("Enter a URL: ")

if not url.startswith(("http:", "https:")):
    raise ValueError("URL must start with 'http:' or 'https:'")

with urlopen(url) as response:
    ...
```

## [References](#references)

* [Python documentation: `urlopen`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen)