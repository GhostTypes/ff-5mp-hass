# [subprocess-without-shell-equals-true (S603)](#subprocess-without-shell-equals-true-s603)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27subprocess-without-shell-equals-true%27%20OR%20S603)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L82)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Check for method calls that initiate a subprocess without a shell.

## [Why is this bad?](#why-is-this-bad)

Starting a subprocess without a shell can prevent attackers from executing
arbitrary shell commands; however, it is still error-prone. Consider
validating the input.

## [Known problems](#known-problems)

Prone to false positives as it is difficult to determine whether the
passed arguments have been validated ([#4045](https://github.com/astral-sh/ruff/issues/4045)).

## [Example](#example)

```
import subprocess

cmd = input("Enter a command: ").split()
subprocess.run(cmd)
```

## [References](#references)

* [Python documentation: `subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)