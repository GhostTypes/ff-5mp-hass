# [suspicious-lxml-import (S410)](#suspicious-lxml-import-s410)

Removed (since [v0.3.0](https://github.com/astral-sh/ruff/releases/tag/v0.3.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-lxml-import%27%20OR%20S410)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L251)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule was removed as the `lxml` library has been modified to address
known vulnerabilities and unsafe defaults. As such, the `defusedxml`
library is no longer necessary, `defusedxml` has [deprecated](https://github.com/tiran/defusedxml/blob/c7445887f5e1bcea470a16f61369d29870cfcfe1/README.md#defusedxmllxml) its `lxml`
module.

## [What it does](#what-it-does)

Checks for imports of the `lxml` module.

## [Why is this bad?](#why-is-this-bad)

Using various methods from the `lxml` module to parse untrusted XML data is
known to be vulnerable to XML attacks. Replace vulnerable imports with the
equivalent `defusedxml` package.

## [Example](#example)

```
import lxml
```