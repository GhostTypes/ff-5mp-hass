# [unnecessary-paren-on-raise-exception (RSE102)](#unnecessary-paren-on-raise-exception-rse102)

Added in [v0.0.239](https://github.com/astral-sh/ruff/releases/tag/v0.0.239) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-paren-on-raise-exception%27%20OR%20RSE102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_raise%2Frules%2Funnecessary_paren_on_raise_exception.rs#L45)

Derived from the **[flake8-raise](../#flake8-raise-rse)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for unnecessary parentheses on raised exceptions.

## [Why is this bad?](#why-is-this-bad)

If an exception is raised without any arguments, parentheses are not
required, as the `raise` statement accepts either an exception instance
or an exception class (which is then implicitly instantiated).

Removing the parentheses makes the code more concise.

## [Known problems](#known-problems)

Parentheses can only be omitted if the exception is a class, as opposed to
a function call. This rule isn't always capable of distinguishing between
the two.

For example, if you import a function `module.get_exception` from another
module, and `module.get_exception` returns an exception object, this rule will
incorrectly mark the parentheses in `raise module.get_exception()` as
unnecessary.

## [Example](#example)

```
raise TypeError()
```

Use instead:

```
raise TypeError
```

## [Fix Safety](#fix-safety)

This rule's fix is marked as unsafe if removing the parentheses would also remove comments
or if it’s unclear whether the expression is a class or a function call.

## [References](#references)

* [Python documentation: The `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)