# [unused-import (F401)](#unused-import-f401)

Added in [v0.0.18](https://github.com/astral-sh/ruff/releases/tag/v0.0.18) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-import%27%20OR%20F401)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Funused_import.rs#L145)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unused imports.

## [Why is this bad?](#why-is-this-bad)

Unused imports add a performance overhead at runtime, and risk creating
import cycles. They also increase the cognitive load of reading the code.

If an import statement is used to check for the availability or existence
of a module, consider using `importlib.util.find_spec` instead.

If an import statement is used to re-export a symbol as part of a module's
public interface, consider using a "redundant" import alias, which
instructs Ruff (and other tools) to respect the re-export, and avoid
marking it as unused, as in:

```
from module import member as member
```

Alternatively, you can use `__all__` to declare a symbol as part of the module's
interface, as in:

```
# __init__.py
import some_module

__all__ = ["some_module"]
```

## [Preview](#preview)

When [preview](https://docs.astral.sh/ruff/preview/) is enabled (and certain simplifying assumptions
are met), we analyze all import statements for a given module
when determining whether an import is used, rather than simply
the last of these statements. This can result in both different and
more import statements being marked as unused.

For example, if a module consists of

```
import a
import a.b
```

then both statements are marked as unused under [preview](https://docs.astral.sh/ruff/preview/), whereas
only the second is marked as unused under stable behavior.

As another example, if a module consists of

```
import a.b
import a

a.b.foo()
```

then a diagnostic will only be emitted for the first line under [preview](https://docs.astral.sh/ruff/preview/),
whereas a diagnostic would only be emitted for the second line under
stable behavior.

Note that this behavior is somewhat subjective and is designed
to conform to the developer's intuition rather than Python's actual
execution. To wit, the statement `import a.b` automatically executes
`import a`, so in some sense `import a` is *always* redundant
in the presence of `import a.b`.

## [Fix safety](#fix-safety)

Fixes to remove unused imports are safe, except in `__init__.py` files.

Applying fixes to `__init__.py` files is currently in preview. The fix offered depends on the
type of the unused import. Ruff will suggest a safe fix to export first-party imports with
either a redundant alias or, if already present in the file, an `__all__` entry. If multiple
`__all__` declarations are present, Ruff will not offer a fix. Ruff will suggest an unsafe fix
to remove third-party and standard library imports -- the fix is unsafe because the module's
interface changes.

See [this FAQ section](https://docs.astral.sh/ruff/faq/#how-does-ruff-determine-which-of-my-imports-are-first-party-third-party-etc)
for more details on how Ruff
determines whether an import is first or third-party.

## [Example](#example)

```
import numpy as np  # unused import


def area(radius):
    return 3.14 * radius**2
```

Use instead:

```
def area(radius):
    return 3.14 * radius**2
```

To check the availability of a module, use `importlib.util.find_spec`:

```
from importlib.util import find_spec

if find_spec("numpy") is not None:
    print("numpy is installed")
else:
    print("numpy is not installed")
```

## [Options](#options)

* [`lint.ignore-init-module-imports`](../../settings/#lint_ignore-init-module-imports)
* [`lint.pyflakes.allowed-unused-imports`](../../settings/#lint_pyflakes_allowed-unused-imports)

## [References](#references)

* [Python documentation: `import`](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
* [Python documentation: `importlib.util.find_spec`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec)
* [Typing documentation: interface conventions](https://typing.python.org/en/latest/spec/distributing.html#library-interface-public-and-private-symbols)