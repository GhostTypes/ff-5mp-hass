# [suspicious-xml-etree-import (S405)](#suspicious-xml-etree-import-s405)

Preview (since [v0.1.12](https://github.com/astral-sh/ruff/releases/tag/v0.1.12)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-xml-etree-import%27%20OR%20S405)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_imports.rs#L124)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for imports of the `xml.etree.cElementTree` and `xml.etree.ElementTree` modules

## [Why is this bad?](#why-is-this-bad)

Using various methods from these modules to parse untrusted XML data is
known to be vulnerable to XML attacks. Replace vulnerable imports with the
equivalent `defusedxml` package, or make sure `defusedxml.defuse_stdlib()` is
called before parsing XML data.

## [Example](#example)

```
import xml.etree.cElementTree
```