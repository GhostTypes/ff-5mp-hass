# [subprocess-popen-with-shell-equals-true (S602)](#subprocess-popen-with-shell-equals-true-s602)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27subprocess-popen-with-shell-equals-true%27%20OR%20S602)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L39)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Check for method calls that initiate a subprocess with a shell.

## [Why is this bad?](#why-is-this-bad)

Starting a subprocess with a shell can allow attackers to execute arbitrary
shell commands. Consider starting the process without a shell call and
sanitize the input to mitigate the risk of shell injection.

## [Example](#example)

```
import subprocess

subprocess.run("ls -l", shell=True)
```

Use instead:

```
import subprocess

subprocess.run(["ls", "-l"])
```

## [References](#references)

* [Python documentation: `subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)
* [Common Weakness Enumeration: CWE-78](https://cwe.mitre.org/data/definitions/78.html)