# [function-call-in-default-argument (B008)](#function-call-in-default-argument-b008)

Added in [v0.0.102](https://github.com/astral-sh/ruff/releases/tag/v0.0.102) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27function-call-in-default-argument%27%20OR%20B008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Ffunction_call_in_argument_default.rs#L64)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for function calls in default function arguments.

## [Why is this bad?](#why-is-this-bad)

Any function call that's used in a default argument will only be performed
once, at definition time. The returned value will then be reused by all
calls to the function, which can lead to unexpected behaviour.

Parameters with immutable type annotations will be ignored by this rule.
Those whose default arguments are `NewType` calls where the original type
is immutable are also ignored.

Calls and types outside of the standard library can be marked as an exception
to this rule with the [`lint.flake8-bugbear.extend-immutable-calls`](../../settings/#lint_flake8-bugbear_extend-immutable-calls) configuration option.

## [Example](#example)

```
def create_list() -> list[int]:
    return [1, 2, 3]


def mutable_default(arg: list[int] = create_list()) -> list[int]:
    arg.append(4)
    return arg
```

Use instead:

```
def better(arg: list[int] | None = None) -> list[int]:
    if arg is None:
        arg = create_list()

    arg.append(4)
    return arg
```

If the use of a singleton is intentional, assign the result call to a
module-level variable, and use that variable in the default argument:

```
ERROR = ValueError("Hosts weren't successfully added")


def add_host(error: Exception = ERROR) -> None: ...
```

## [Options](#options)

* [`lint.flake8-bugbear.extend-immutable-calls`](../../settings/#lint_flake8-bugbear_extend-immutable-calls)