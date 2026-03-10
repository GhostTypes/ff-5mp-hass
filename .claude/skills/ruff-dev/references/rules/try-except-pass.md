# [try-except-pass (S110)](#try-except-pass-s110)

Added in [v0.0.237](https://github.com/astral-sh/ruff/releases/tag/v0.0.237) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27try-except-pass%27%20OR%20S110)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Ftry_except_pass.rs#L43)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the `try`-`except`-`pass` pattern.

## [Why is this bad?](#why-is-this-bad)

The `try`-`except`-`pass` pattern suppresses all exceptions. Suppressing
exceptions may hide errors that could otherwise reveal unexpected behavior,
security vulnerabilities, or malicious activity. Instead, consider logging
the exception.

## [Example](#example)

```
try:
    ...
except Exception:
    pass
```

Use instead:

```
import logging

try:
    ...
except Exception as exc:
    logging.exception("Exception occurred")
```

## [Options](#options)

* [`lint.flake8-bandit.check-typed-exception`](../../settings/#lint_flake8-bandit_check-typed-exception)

## [References](#references)

* [Common Weakness Enumeration: CWE-703](https://cwe.mitre.org/data/definitions/703.html)
* [Python documentation: `logging`](https://docs.python.org/3/library/logging.html)