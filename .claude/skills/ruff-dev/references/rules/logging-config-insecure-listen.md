# [logging-config-insecure-listen (S612)](#logging-config-insecure-listen-s612)

Added in [v0.0.231](https://github.com/astral-sh/ruff/releases/tag/v0.0.231) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27logging-config-insecure-listen%27%20OR%20S612)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Flogging_config_insecure_listen.rs#L27)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for insecure `logging.config.listen` calls.

## [Why is this bad?](#why-is-this-bad)

`logging.config.listen` starts a server that listens for logging
configuration requests. This is insecure, as parts of the configuration are
passed to the built-in `eval` function, which can be used to execute
arbitrary code.

## [Example](#example)

```
import logging

logging.config.listen(9999)
```

## [References](#references)

* [Python documentation: `logging.config.listen()`](https://docs.python.org/3/library/logging.config.html#logging.config.listen)