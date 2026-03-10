# [shallow-copy-environ (PLW1507)](#shallow-copy-environ-plw1507)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27shallow-copy-environ%27%20OR%20PLW1507)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fshallow_copy_environ.rs#L45)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Check for shallow `os.environ` copies.

## [Why is this bad?](#why-is-this-bad)

`os.environ` is not a `dict` object, but rather, a proxy object. As such, mutating a shallow
copy of `os.environ` will also mutate the original object.

See [BPO 15373](https://bugs.python.org/issue15373) for more information.

## [Example](#example)

```
import copy
import os

env = copy.copy(os.environ)
```

Use instead:

```
import os

env = os.environ.copy()
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because replacing a shallow copy with a deep copy can lead
to unintended side effects. If the program modifies the shallow copy at some point, changing it
to a deep copy may prevent those modifications from affecting the original data, potentially
altering the program's behavior.

## [References](#references)

* [Python documentation: `copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
* [Python documentation: `os.environ`](https://docs.python.org/3/library/os.html#os.environ)