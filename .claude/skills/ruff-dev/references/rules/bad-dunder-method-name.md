# [bad-dunder-method-name (PLW3201)](#bad-dunder-method-name-plw3201)

Preview (since [v0.0.285](https://github.com/astral-sh/ruff/releases/tag/v0.0.285)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-dunder-method-name%27%20OR%20PLW3201)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_dunder_method_name.rs#L47)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for dunder methods that have no special meaning in Python 3.

## [Why is this bad?](#why-is-this-bad)

Misspelled or no longer supported dunder name methods may cause your code to not function
as expected.

Since dunder methods are associated with customizing the behavior
of a class in Python, introducing a dunder method such as `__foo__`
that diverges from standard Python dunder methods could potentially
confuse someone reading the code.

This rule will detect all methods starting and ending with at least
one underscore (e.g., `_str_`), but ignores known dunder methods (like
`__init__`), as well as methods that are marked with [`@override`](https://docs.python.org/3/library/typing.html#typing.override).

Additional dunder methods names can be allowed via the
[`lint.pylint.allow-dunder-method-names`](../../settings/#lint_pylint_allow-dunder-method-names) setting.

## [Example](#example)

```
class Foo:
    def __init_(self): ...
```

Use instead:

```
class Foo:
    def __init__(self): ...
```

## [Options](#options)

* [`lint.pylint.allow-dunder-method-names`](../../settings/#lint_pylint_allow-dunder-method-names)