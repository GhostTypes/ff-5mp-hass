# [invalid-all-format (PLE0605)](#invalid-all-format-ple0605)

Added in [v0.0.237](https://github.com/astral-sh/ruff/releases/tag/v0.0.237) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-all-format%27%20OR%20PLE0605)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Finvalid_all_format.rs#L29)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for invalid assignments to `__all__`.

## [Why is this bad?](#why-is-this-bad)

In Python, `__all__` should contain a sequence of strings that represent
the names of all "public" symbols exported by a module.

Assigning anything other than a `tuple` or `list` of strings to `__all__`
is invalid.

## [Example](#example)

```
__all__ = "Foo"
```

Use instead:

```
__all__ = ("Foo",)
```

## [References](#references)

* [Python documentation: The `import` statement](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)