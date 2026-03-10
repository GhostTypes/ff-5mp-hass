# [error-suffix-on-exception-name (N818)](#error-suffix-on-exception-name-n818)

Added in [v0.0.89](https://github.com/astral-sh/ruff/releases/tag/v0.0.89) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27error-suffix-on-exception-name%27%20OR%20N818)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Ferror_suffix_on_exception_name.rs#L37)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for custom exception definitions that omit the `Error` suffix.

## [Why is this bad?](#why-is-this-bad)

The `Error` suffix is recommended by [PEP 8](https://peps.python.org/pep-0008/#exception-names):

> Because exceptions should be classes, the class naming convention
> applies here. However, you should use the suffix `"Error"` on your
> exception names (if the exception actually is an error).

## [Example](#example)

```
class Validation(Exception): ...
```

Use instead:

```
class ValidationError(Exception): ...
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)