# [suspicious-pycrypto-import (S413)](#suspicious-pycrypto-import-s413)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-pycrypto-import%27%20OR%20S413)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L328)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of several unsafe cryptography modules.

## [Why is this bad?](#why-is-this-bad)

The `pycrypto` library is known to have a publicly disclosed buffer
overflow vulnerability. It is no longer actively maintained and has been
deprecated in favor of the `pyca/cryptography` library.

## [Example](#example)

```
import Crypto.Random
```

## [References](#references)

* [Buffer Overflow Issue](https://github.com/pycrypto/pycrypto/issues/176)