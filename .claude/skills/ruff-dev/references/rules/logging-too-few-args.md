# [logging-too-few-args (PLE1206)](#logging-too-few-args-ple1206)

Added in [v0.0.252](https://github.com/astral-sh/ruff/releases/tag/v0.0.252) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27logging-too-few-args%27%20OR%20PLE1206)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Flogging.rs#L39)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for too few positional arguments for a `logging` format string.

## [Why is this bad?](#why-is-this-bad)

A `TypeError` will be raised if the statement is run.

## [Example](#example)

```
import logging

try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", e)
    raise
```

Use instead:

```
import logging

try:
    function()
except Exception as e:
    logging.error("%s error occurred: %s", type(e), e)
    raise
```