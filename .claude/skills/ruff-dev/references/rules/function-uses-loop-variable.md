# [function-uses-loop-variable (B023)](#function-uses-loop-variable-b023)

Added in [v0.0.139](https://github.com/astral-sh/ruff/releases/tag/v0.0.139) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27function-uses-loop-variable%27%20OR%20B023)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Ffunction_uses_loop_variable.rs#L44)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for function definitions that use a loop variable.

## [Why is this bad?](#why-is-this-bad)

The loop variable is not bound in the function definition, so it will always
have the value it had in the last iteration when the function is called.

Instead, consider using a default argument to bind the loop variable at
function definition time. Or, use `functools.partial`.

## [Example](#example)

```
adders = [lambda x: x + i for i in range(3)]
values = [adder(1) for adder in adders]  # [3, 3, 3]
```

Use instead:

```
adders = [lambda x, i=i: x + i for i in range(3)]
values = [adder(1) for adder in adders]  # [1, 2, 3]
```

Or:

```
from functools import partial

adders = [partial(lambda x, i: x + i, i=i) for i in range(3)]
values = [adder(1) for adder in adders]  # [1, 2, 3]
```

## [References](#references)

* [The Hitchhiker's Guide to Python: Late Binding Closures](https://docs.python-guide.org/writing/gotchas/#late-binding-closures)
* [Python documentation: `functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial)