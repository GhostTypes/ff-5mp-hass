# [nonlocal-without-binding (PLE0117)](#nonlocal-without-binding-ple0117)

Added in [v0.0.174](https://github.com/astral-sh/ruff/releases/tag/v0.0.174) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27nonlocal-without-binding%27%20OR%20PLE0117)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fnonlocal_without_binding.rs#L33)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `nonlocal` names without bindings.

## [Why is this bad?](#why-is-this-bad)

`nonlocal` names must be bound to a name in an outer scope.
Violating this rule leads to a `SyntaxError` at runtime.

## [Example](#example)

```
def foo():
    def get_bar(self):
        nonlocal bar
        ...
```

Use instead:

```
def foo():
    bar = 1

    def get_bar(self):
        nonlocal bar
        ...
```

## [References](#references)

* [Python documentation: The `nonlocal` statement](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)
* [PEP 3104 – Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)