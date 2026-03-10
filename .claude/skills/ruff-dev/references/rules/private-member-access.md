# [private-member-access (SLF001)](#private-member-access-slf001)

Added in [v0.0.240](https://github.com/astral-sh/ruff/releases/tag/v0.0.240) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27private-member-access%27%20OR%20SLF001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_self%2Frules%2Fprivate_member_access.rs#L57)

Derived from the **[flake8-self](../#flake8-self-slf)** linter.

## [What it does](#what-it-does)

Checks for accesses on "private" class members.

## [Why is this bad?](#why-is-this-bad)

In Python, the convention is such that class members that are prefixed
with a single underscore, or prefixed but not suffixed with a double
underscore, are considered private and intended for internal use.

Using such "private" members is considered a misuse of the class, as
there are no guarantees that the member will be present in future
versions, that it will have the same type, or that it will have the same
behavior. Instead, use the class's public interface.

This rule ignores accesses on dunder methods (e.g., `__init__`) and sunder
methods (e.g., `_missing_`).

## [Example](#example)

```
class Class:
    def __init__(self):
        self._private_member = "..."


var = Class()
print(var._private_member)
```

Use instead:

```
class Class:
    def __init__(self):
        self.public_member = "..."


var = Class()
print(var.public_member)
```

## [Options](#options)

* [`lint.flake8-self.ignore-names`](../../settings/#lint_flake8-self_ignore-names)

## [References](#references)

* [*What is the meaning of single or double underscores before an object name?*](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name)