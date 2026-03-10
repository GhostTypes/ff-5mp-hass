# [call-with-shell-equals-true (S604)](#call-with-shell-equals-true-s604)

Added in [v0.0.262](https://github.com/astral-sh/ruff/releases/tag/v0.0.262) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27call-with-shell-equals-true%27%20OR%20S604)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fshell_injection.rs#L121)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for method calls that set the `shell` parameter to `true` or another
truthy value when invoking a subprocess.

## [Why is this bad?](#why-is-this-bad)

Setting the `shell` parameter to `true` or another truthy value when
invoking a subprocess can introduce security vulnerabilities, as it allows
shell metacharacters and whitespace to be passed to child processes,
potentially leading to shell injection attacks.

It is recommended to avoid using `shell=True` unless absolutely necessary
and, when used, to ensure that all inputs are properly sanitized and quoted
to prevent such vulnerabilities.

## [Known problems](#known-problems)

Prone to false positives as it is triggered on any function call with a
`shell=True` parameter.

## [Example](#example)

```
import my_custom_subprocess

user_input = input("Enter a command: ")
my_custom_subprocess.run(user_input, shell=True)
```

## [References](#references)

* [Python documentation: Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)