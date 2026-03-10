# [yield-outside-function (F704)](#yield-outside-function-f704)

Added in [v0.0.22](https://github.com/astral-sh/ruff/releases/tag/v0.0.22) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27yield-outside-function%27%20OR%20F704)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyflakes%2Frules%2Fyield_outside_function.rs#L56)

Derived from the **[Pyflakes](../#pyflakes-f)** linter.

## [What it does](#what-it-does)

Checks for `yield`, `yield from`, and `await` usages outside of functions.

## [Why is this bad?](#why-is-this-bad)

The use of `yield`, `yield from`, or `await` outside of a function will
raise a `SyntaxError`.

## [Example](#example)

```
class Foo:
    yield 1
```

## [Notebook behavior](#notebook-behavior)

As an exception, `await` is allowed at the top level of a Jupyter notebook
(see: [autoawait](https://ipython.readthedocs.io/en/stable/interactive/autoawait.html)).

## [References](#references)

* [Python documentation: `yield`](https://docs.python.org/3/reference/simple_stmts.html#the-yield-statement)