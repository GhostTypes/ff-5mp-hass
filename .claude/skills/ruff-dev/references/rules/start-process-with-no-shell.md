# [start-process-with-no-shell (S606)](#start-process-with-no-shell-s606)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27start-process-with-no-shell%27%20OR%20S606)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L216)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for functions that start a process without a shell.

## [Why is this bad?](#why-is-this-bad)

Invoking any kind of external executable via a function call can pose
security risks if arbitrary variables are passed to the executable, or if
the input is otherwise unsanitised or unvalidated.

This rule specifically flags functions in the `os` module that spawn
subprocesses *without* the use of a shell. Note that these typically pose a
much smaller security risk than subprocesses that are started *with* a
shell, which are flagged by [`start-process-with-a-shell`](https://docs.astral.sh/ruff/rules/start-process-with-a-shell) (`S605`).
This gives you the option of enabling one rule while disabling the other
if you decide that the security risk from these functions is acceptable
for your use case.

## [Example](#example)

```
import os


def insecure_function(arbitrary_user_input: str):
    os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", arbitrary_user_input)
```