# [byte-string-usage (PYI057)](#byte-string-usage-pyi057)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27byte-string-usage%27%20OR%20PYI057)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fbytestring_usage.rs#L30)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

## [What it does](#what-it-does)

Checks for uses of `typing.ByteString` or `collections.abc.ByteString`.

## [Why is this bad?](#why-is-this-bad)

`ByteString` has been deprecated since Python 3.9 and will be removed in
Python 3.14. The Python documentation recommends using either
`collections.abc.Buffer` (or the `typing_extensions` backport
on Python \<3.12) or a union like `bytes | bytearray | memoryview` instead.

## [Example](#example)

```
from typing import ByteString
```

Use instead:

```
from collections.abc import Buffer
```

## [References](#references)

* [Python documentation: The `ByteString` type](https://docs.python.org/3/library/typing.html#typing.ByteString)