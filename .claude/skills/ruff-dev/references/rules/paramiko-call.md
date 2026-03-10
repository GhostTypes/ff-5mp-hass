# [paramiko-call (S601)](#paramiko-call-s601)

Added in [v0.0.270](https://github.com/astral-sh/ruff/releases/tag/v0.0.270) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27paramiko-call%27%20OR%20S601)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fparamiko_calls.rs#L28)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for `paramiko` calls.

## [Why is this bad?](#why-is-this-bad)

`paramiko` calls allow users to execute arbitrary shell commands on a
remote machine. If the inputs to these calls are not properly sanitized,
they can be vulnerable to shell injection attacks.

## [Example](#example)

```
import paramiko

client = paramiko.SSHClient()
client.exec_command("echo $HOME")
```

## [References](#references)

* [Common Weakness Enumeration: CWE-78](https://cwe.mitre.org/data/definitions/78.html)
* [Paramiko documentation: `SSHClient.exec_command()`](https://docs.paramiko.org/en/stable/api/client.html#paramiko.client.SSHClient.exec_command)