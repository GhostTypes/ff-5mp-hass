# [unix-command-wildcard-injection (S609)](#unix-command-wildcard-injection-s609)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unix-command-wildcard-injection%27%20OR%20S609)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L286)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for possible wildcard injections in calls to `subprocess.Popen()`.

## [Why is this bad?](#why-is-this-bad)

Wildcard injections can lead to unexpected behavior if unintended files are
matched by the wildcard. Consider using a more specific path instead.

## [Example](#example)

```
import subprocess

subprocess.Popen(["chmod", "777", "*.py"], shell=True)
```

Use instead:

```
import subprocess

subprocess.Popen(["chmod", "777", "main.py"], shell=True)
```

## [References](#references)

* [Common Weakness Enumeration: CWE-78](https://cwe.mitre.org/data/definitions/78.html)