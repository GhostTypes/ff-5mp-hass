# [unnecessary-placeholder (PIE790)](#unnecessary-placeholder-pie790)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-placeholder%27%20OR%20PIE790)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Funnecessary_placeholder.rs#L59)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary `pass` statements and ellipsis (`...`) literals in
functions, classes, and other blocks.

## [Why is this bad?](#why-is-this-bad)

In Python, the `pass` statement and ellipsis (`...`) literal serve as
placeholders, allowing for syntactically correct empty code blocks. The
primary purpose of these nodes is to avoid syntax errors in situations
where a statement or expression is syntactically required, but no code
needs to be executed.

If a `pass` or ellipsis is present in a code block that includes at least
one other statement (even, e.g., a docstring), it is unnecessary and should
be removed.

## [Example](#example)

```
def func():
    """Placeholder docstring."""
    pass
```

Use instead:

```
def func():
    """Placeholder docstring."""
```

Or, given:

```
def func():
    """Placeholder docstring."""
    ...
```

Use instead:

```
def func():
    """Placeholder docstring."""
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe in the rare case that the `pass` or ellipsis
is followed by a string literal, since removal of the placeholder would convert the
subsequent string literal into a docstring.

## [References](#references)

* [Python documentation: The `pass` statement](https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement)