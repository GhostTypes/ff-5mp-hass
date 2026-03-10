# [exec-builtin (S102)](#exec-builtin-s102)

Added in [v0.0.116](https://github.com/astral-sh/ruff/releases/tag/v0.0.116) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27exec-builtin%27%20OR%20S102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fexec_used.rs#L24)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the builtin `exec` function.

## [Why is this bad?](#why-is-this-bad)

The `exec()` function is insecure as it allows for arbitrary code
execution.

## [Example](#example)

```
exec("print('Hello World')")
```

## [References](#references)

* [Python documentation: `exec`](https://docs.python.org/3/library/functions.html#exec)
* [Common Weakness Enumeration: CWE-78](https://cwe.mitre.org/data/definitions/78.html)