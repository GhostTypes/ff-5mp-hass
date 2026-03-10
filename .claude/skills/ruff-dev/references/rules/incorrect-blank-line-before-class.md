# [incorrect-blank-line-before-class (D203)](#incorrect-blank-line-before-class-d203)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27incorrect-blank-line-before-class%27%20OR%20D203)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fblank_before_after_class.rs#L45)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for docstrings on class definitions that are not preceded by a
blank line.

## [Why is this bad?](#why-is-this-bad)

Use a blank line to separate the docstring from the class definition, for
consistency.

This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is disabled when using the `google`,
`numpy`, and `pep257` conventions.

For an alternative, see [D211](https://docs.astral.sh/ruff/rules/blank-line-before-class).

## [Example](#example)

```
class PhotoMetadata:
    """Metadata about a photo."""
```

Use instead:

```
class PhotoMetadata:

    """Metadata about a photo."""
```

## [Options](#options)

* [`lint.pydocstyle.convention`](../../settings/#lint_pydocstyle_convention)