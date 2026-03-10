# [suspicious-eval-usage (S307)](#suspicious-eval-usage-s307)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27suspicious-eval-usage%27%20OR%20S307)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bandit%2Frules%2Fsuspicious_function_call.rs#L338)

Derived from the **[flake8-bandit](../#flake8-bandit-s)** linter.

## [What it does](#what-it-does)

Checks for uses of the builtin `eval()` function.

## [Why is this bad?](#why-is-this-bad)

The `eval()` function is insecure as it enables arbitrary code execution.

If you need to evaluate an expression from a string, consider using
`ast.literal_eval()` instead, which will raise an exception if the
expression is not a valid Python literal.

In [preview](https://docs.astral.sh/ruff/preview/), this rule will also flag references to `eval`.

## [Example](#example)

```
x = eval(input("Enter a number: "))
```

Use instead:

```
from ast import literal_eval

x = literal_eval(input("Enter a number: "))
```

## [References](#references)

* [Python documentation: `eval`](https://docs.python.org/3/library/functions.html#eval)
* [Python documentation: `literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval)
* [*Eval really is dangerous* by Ned Batchelder](https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html)