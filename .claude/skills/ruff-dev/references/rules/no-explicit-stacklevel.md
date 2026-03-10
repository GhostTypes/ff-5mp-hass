# [no-explicit-stacklevel (B028)](#no-explicit-stacklevel-b028)

Added in [v0.0.257](https://github.com/astral-sh/ruff/releases/tag/v0.0.257) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-explicit-stacklevel%27%20OR%20B028)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fno_explicit_stacklevel.rs#L43)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for `warnings.warn` calls without an explicit `stacklevel` keyword
argument.

## [Why is this bad?](#why-is-this-bad)

The `warnings.warn` method uses a `stacklevel` of 1 by default, which
will output a stack frame of the line on which the "warn" method
is called. Setting it to a higher number will output a stack frame
from higher up the stack.

It's recommended to use a `stacklevel` of 2 or higher, to give the caller
more context about the warning.

## [Example](#example)

```
import warnings

warnings.warn("This is a warning")
```

Use instead:

```
import warnings

warnings.warn("This is a warning", stacklevel=2)
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because it changes
the behavior of the code. Moreover, the fix will assign
a stacklevel of 2, while the user may wish to assign a
higher stacklevel to address the diagnostic.

## [References](#references)

* [Python documentation: `warnings.warn`](https://docs.python.org/3/library/warnings.html#warnings.warn)