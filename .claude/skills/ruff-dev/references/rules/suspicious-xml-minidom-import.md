# [suspicious-xml-minidom-import (S408)](#suspicious-xml-minidom-import-s408)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-xml-minidom-import%27%20OR%20S408)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L196)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `xml.dom.minidom` module.

## [Why is this bad?](#why-is-this-bad)

Using various methods from these modules to parse untrusted XML data is
known to be vulnerable to XML attacks. Replace vulnerable imports with the
equivalent `defusedxml` package, or make sure `defusedxml.defuse_stdlib()` is
called before parsing XML data.

## [Example](#example)

```
import xml.dom.minidom
```