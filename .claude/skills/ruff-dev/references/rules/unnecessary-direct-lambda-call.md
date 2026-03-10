# [unnecessary-direct-lambda-call (PLC3002)](#unnecessary-direct-lambda-call-plc3002)

Added in [v0.0.153](https://github.com/astral-sh/ruff/releases/tag/v0.0.153) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-direct-lambda-call%27%20OR%20PLC3002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funnecessary_direct_lambda_call.rs#L28)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for unnecessary direct calls to lambda expressions.

## [Why is this bad?](#why-is-this-bad)

Calling a lambda expression directly is unnecessary. The expression can be
executed inline instead to improve readability.

## [Example](#example)

```
area = (lambda r: 3.14 * r**2)(radius)
```

Use instead:

```
area = 3.14 * radius**2
```

## [References](#references)

* [Python documentation: Lambdas](https://docs.python.org/3/reference/expressions.html#lambda)