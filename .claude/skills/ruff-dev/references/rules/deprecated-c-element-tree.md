# [deprecated-c-element-tree (UP023)](#deprecated-c-element-tree-up023)

Added in [v0.0.199](https://github.com/astral-sh/ruff/releases/tag/v0.0.199) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27deprecated-c-element-tree%27%20OR%20UP023)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fdeprecated_c_element_tree.rs#L27)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of the `xml.etree.cElementTree` module.

## [Why is this bad?](#why-is-this-bad)

In Python 3.3, `xml.etree.cElementTree` was deprecated in favor of
`xml.etree.ElementTree`.

## [Example](#example)

```
from xml.etree import cElementTree as ET
```

Use instead:

```
from xml.etree import ElementTree as ET
```

## [References](#references)

* [Python documentation: `xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html)