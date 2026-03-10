# [suspicious-pickle-import (S403)](#suspicious-pickle-import-s403)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-pickle-import%27%20OR%20S403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L78)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `pickle`, `cPickle`, `dill`, and `shelve` modules.

## [Why is this bad?](#why-is-this-bad)

It is possible to construct malicious pickle data which will execute
arbitrary code during unpickling. Consider possible security implications
associated with these modules.

## [Example](#example)

```
import pickle
```

## [References](#references)

* [Python documentation: `pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)