# [await-outside-async (PLE1142)](#await-outside-async-ple1142)

Added in [v0.0.150](https://github.com/astral-sh/ruff/releases/tag/v0.0.150) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27await-outside-async%27%20OR%20PLE1142)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fawait_outside_async.rs#L38)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for uses of `await` outside `async` functions.

## [Why is this bad?](#why-is-this-bad)

Using `await` outside an `async` function is a syntax error.

## [Example](#example)

```
import asyncio


def foo():
    await asyncio.sleep(1)
```

Use instead:

```
import asyncio


async def foo():
    await asyncio.sleep(1)
```

## [Notebook behavior](#notebook-behavior)

As an exception, `await` is allowed at the top level of a Jupyter notebook
(see: [autoawait](https://ipython.readthedocs.io/en/stable/interactive/autoawait.html)).

## [References](#references)

* [Python documentation: Await expression](https://docs.python.org/3/reference/expressions.html#await)
* [PEP 492: Await Expression](https://peps.python.org/pep-0492/#await-expression)