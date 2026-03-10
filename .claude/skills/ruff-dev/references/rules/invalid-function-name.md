# [invalid-function-name (N802)](#invalid-function-name-n802)

Added in [v0.0.77](https://github.com/astral-sh/ruff/releases/tag/v0.0.77) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-function-name%27%20OR%20N802)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Finvalid_function_name.rs#L50)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for functions names that do not follow the `snake_case` naming
convention.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names) recommends that function names follow `snake_case`:

> Function names should be lowercase, with words separated by underscores as necessary to
> improve readability. mixedCase is allowed only in contexts where that’s already the
> prevailing style (e.g. threading.py), to retain backwards compatibility.

Names can be excluded from this rule using the [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
or [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names) configuration options. For example,
to ignore all functions starting with `test_` from this rule, set the
[`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names) option to `["test_*"]`.

This rule exempts methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override).
Explicitly decorating a method with `@override` signals to Ruff that the method is intended
to override a superclass method, and that a type checker will enforce that it does so. Ruff
therefore knows that it should not enforce naming conventions on such methods.

## [Example](#example)

```
def myFunction():
    pass
```

Use instead:

```
def my_function():
    pass
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)