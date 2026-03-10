# [subclass-builtin (FURB189)](#subclass-builtin-furb189)

Preview (since [0.7.3](https://github.com/astral-sh/ruff/releases/tag/0.7.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27subclass-builtin%27%20OR%20FURB189)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fsubclass_builtin.rs#L59)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for subclasses of `dict`, `list` or `str`.

## [Why is this bad?](#why-is-this-bad)

Built-in types don't consistently use their own dunder methods. For example,
`dict.__init__` and `dict.update()` bypass `__setitem__`, making inheritance unreliable.

Use the `UserDict`, `UserList`, and `UserString` objects from the `collections` module
instead.

## [Example](#example)

```
class UppercaseDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


d = UppercaseDict({"a": 1, "b": 2})  # Bypasses __setitem__
print(d)  # {'a': 1, 'b': 2}
```

Use instead:

```
from collections import UserDict


class UppercaseDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


d = UppercaseDict({"a": 1, "b": 2})  # Uses __setitem__
print(d)  # {'A': 1, 'B': 2}
```

## [Fix safety](#fix-safety)

This fix is marked as unsafe because `isinstance()` checks for `dict`,
`list`, and `str` types will fail when using the corresponding User class.
If you need to pass custom `dict` or `list` objects to code you don't
control, ignore this check. If you do control the code, consider using
the following type checks instead:

* `dict` -> `collections.abc.MutableMapping`
* `list` -> `collections.abc.MutableSequence`
* `str` -> No such conversion exists

## [References](#references)

* [Python documentation: `collections`](https://docs.python.org/3/library/collections.html)