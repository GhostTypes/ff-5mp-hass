# [start-process-with-a-shell (S605)](#start-process-with-a-shell-s605)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27start-process-with-a-shell%27%20OR%20S605)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L174)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for calls that start a process with a shell, providing guidance on
whether the usage is safe or not.

## [Why is this bad?](#why-is-this-bad)

Starting a process with a shell can introduce security risks, such as
code injection vulnerabilities. It's important to be aware of whether the
usage of the shell is safe or not.

This rule triggers on functions like `os.system`, `popen`, etc., which
start processes with a shell. It evaluates whether the provided command
is a literal string or an expression. If the command is a literal string,
it's considered safe. If the command is an expression, it's considered
(potentially) unsafe.

## [Example](#example)

```
import os

# Safe usage (literal string)
command = "ls -l"
os.system(command)

# Potentially unsafe usage (expression)
cmd = get_user_input()
os.system(cmd)
```

## [Note](#note)

The `subprocess` module provides more powerful facilities for spawning new
processes and retrieving their results, and using that module is preferable
to using `os.system` or similar functions. Consider replacing such usages
with `subprocess.call` or related functions.

## [References](#references)

* [Python documentation: `subprocess`](https://docs.python.org/3/library/subprocess.html)