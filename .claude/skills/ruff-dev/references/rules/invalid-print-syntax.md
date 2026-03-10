# [invalid-print-syntax (F633)](#invalid-print-syntax-f633)

Added in [v0.0.39](https://github.com/astral-sh/ruff/releases/tag/v0.0.39) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-print-syntax%27%20OR%20F633)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Finvalid_print_syntax.rs#L49)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `print` statements that use the `>>` syntax.

## [Why is this bad?](#why-is-this-bad)

In Python 2, the `print` statement can be used with the `>>` syntax to
print to a file-like object. This `print >> sys.stderr` syntax no
longer exists in Python 3, where `print` is only a function, not a
statement.

Instead, use the `file` keyword argument to the `print` function, the
`sys.stderr.write` function, or the `logging` module.

## [Example](#example)

```
from __future__ import print_function
import sys

print >> sys.stderr, "Hello, world!"
```

Use instead:

```
print("Hello, world!", file=sys.stderr)
```

Or:

```
import sys

sys.stderr.write("Hello, world!\n")
```

Or:

```
import logging

logging.error("Hello, world!")
```

## [References](#references)

* [Python documentation: `print`](https://docs.python.org/3/library/functions.html#print)