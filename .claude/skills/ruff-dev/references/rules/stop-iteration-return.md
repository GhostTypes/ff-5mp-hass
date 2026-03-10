# [stop-iteration-return (PLR1708)](#stop-iteration-return-plr1708)

Preview (since [0.14.3](https://github.com/astral-sh/ruff/releases/tag/0.14.3)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27stop-iteration-return%27%20OR%20PLR1708)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fstop_iteration_return.rs#L40)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for explicit `raise StopIteration` in generator functions.

## [Why is this bad?](#why-is-this-bad)

Raising `StopIteration` in a generator function causes a `RuntimeError`
when the generator is iterated over.

Instead of `raise StopIteration`, use `return` in generator functions.

## [Example](#example)

```
def my_generator():
    yield 1
    yield 2
    raise StopIteration  # This causes RuntimeError at runtime
```

Use instead:

```
def my_generator():
    yield 1
    yield 2
    return  # Use return instead
```

## [References](#references)

* [PEP 479](https://peps.python.org/pep-0479/)
* [Python documentation](https://docs.python.org/3/library/exceptions.html#StopIteration)