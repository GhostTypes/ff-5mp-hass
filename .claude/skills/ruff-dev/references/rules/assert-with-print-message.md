# [assert-with-print-message (RUF030)](#assert-with-print-message-ruf030)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27assert-with-print-message%27%20OR%20RUF030)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fassert_with_print_message.rs#L40)

Fix is always available.

## [What it does](#what-it-does)

Checks for uses of `assert expression, print(message)`.

## [Why is this bad?](#why-is-this-bad)

If an `assert x, y` assertion fails, the Python interpreter raises an
`AssertionError`, and the evaluated value of `y` is used as the contents of
that assertion error. The `print` function always returns `None`, however,
so the evaluated value of a call to `print` will always be `None`.

Using a `print` call in this context will therefore output the message to
`stdout`, before raising an empty `AssertionError(None)`. Instead, remove
the `print` and pass the message directly as the second expression,
allowing `stderr` to capture the message in a well-formatted context.

## [Example](#example)

```
assert False, print("This is a message")
```

Use instead:

```
assert False, "This is a message"
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as changing the second expression
will result in a different `AssertionError` message being raised, as well as
a change in `stdout` output.

## [References](#references)

* [Python documentation: `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)