# [suspicious-pyghmi-import (S415)](#suspicious-pyghmi-import-s415)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-pyghmi-import%27%20OR%20S415)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L354)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `pyghmi` module.

## [Why is this bad?](#why-is-this-bad)

`pyghmi` is an IPMI-related module, but IPMI is considered insecure.
Instead, use an encrypted protocol.

## [Example](#example)

```
import pyghmi
```

## [References](#references)

* [Buffer Overflow Issue](https://github.com/pycrypto/pycrypto/issues/176)