# [raise-vanilla-args (TRY003)](#raise-vanilla-args-try003)

Added in [v0.0.236](https://github.com/astral-sh/ruff/releases/tag/v0.0.236) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-vanilla-args%27%20OR%20TRY003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Fraise_vanilla_args.rs#L46)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

## [What it does](#what-it-does)

Checks for long exception messages that are not defined in the exception
class itself.

## [Why is this bad?](#why-is-this-bad)

By formatting an exception message at the `raise` site, the exception class
becomes less reusable, and may now raise inconsistent messages depending on
where it is raised.

If the exception message is instead defined within the exception class, it
will be consistent across all `raise` invocations.

This rule is not enforced for some built-in exceptions that are commonly
raised with a message and would be unusual to subclass, such as
`NotImplementedError`.

## [Example](#example)

```
class CantBeNegative(Exception):
    pass


def foo(x):
    if x < 0:
        raise CantBeNegative(f"{x} is negative")
```

Use instead:

```
class CantBeNegative(Exception):
    def __init__(self, number):
        super().__init__(f"{number} is negative")


def foo(x):
    if x < 0:
        raise CantBeNegative(x)
```