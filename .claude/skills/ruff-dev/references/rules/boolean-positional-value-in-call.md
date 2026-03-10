# [boolean-positional-value-in-call (FBT003)](#boolean-positional-value-in-call-fbt003)

Added in [v0.0.127](https://github.com/astral-sh/ruff/releases/tag/v0.0.127) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27boolean-positional-value-in-call%27%20OR%20FBT003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_boolean_trap%2Frules%2Fboolean_positional_value_in_call.rs#L44)

Derived from the **[flake8-boolean-trap](../#flake8-boolean-trap-fbt)** linter.

## [What it does](#what-it-does)

Checks for boolean positional arguments in function calls.

Some functions are whitelisted by default. To extend the list of allowed calls
configure the [`lint.flake8-boolean-trap.extend-allowed-calls`](../../settings/#lint_flake8-boolean-trap_extend-allowed-calls) option.

## [Why is this bad?](#why-is-this-bad)

Calling a function with boolean positional arguments is confusing as the
meaning of the boolean value is not clear to the caller, and to future
readers of the code.

## [Example](#example)

```
def func(flag: bool) -> None: ...


func(True)
```

Use instead:

```
def func(flag: bool) -> None: ...


func(flag=True)
```

## [Options](#options)

* [`lint.flake8-boolean-trap.extend-allowed-calls`](../../settings/#lint_flake8-boolean-trap_extend-allowed-calls)

## [References](#references)

* [Python documentation: Calls](https://docs.python.org/3/reference/expressions.html#calls)
* [*How to Avoid “The Boolean Trap”* by Adam Johnson](https://adamj.eu/tech/2021/07/10/python-type-hints-how-to-avoid-the-boolean-trap/)