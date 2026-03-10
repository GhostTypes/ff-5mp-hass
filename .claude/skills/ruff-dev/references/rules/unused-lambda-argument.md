# [unused-lambda-argument (ARG005)](#unused-lambda-argument-arg005)

Added in [v0.0.168](https://github.com/astral-sh/ruff/releases/tag/v0.0.168) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-lambda-argument%27%20OR%20ARG005)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_unused_arguments%2Frules%2Funused_arguments.rs#L241)

Derived from the **[flake8-unused-arguments](../#flake8-unused-arguments-arg)** linter.

## [What it does](#what-it-does)

Checks for the presence of unused arguments in lambda expression
definitions.

## [Why is this bad?](#why-is-this-bad)

An argument that is defined but not used is likely a mistake, and should
be removed to avoid confusion.

If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
[`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) pattern.

## [Example](#example)

```
my_list = [1, 2, 3, 4, 5]
squares = map(lambda x, y: x**2, my_list)
```

Use instead:

```
my_list = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, my_list)
```

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)