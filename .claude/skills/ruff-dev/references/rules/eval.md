# [eval (PGH001)](#eval-pgh001)

Removed (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27eval%27%20OR%20PGH001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpygrep_hooks%2Frules%2Fno_eval.rs#L33)

Derived from the **[pygrep-hooks](../#pygrep-hooks-pgh)** linter.

**Warning: This rule has been removed and its documentation is only available for historical reasons.**

## [Removed](#removed)

This rule is identical to [S307](https://docs.astral.sh/ruff/rules/suspicious-eval-usage/) which should be used instead.

## [What it does](#what-it-does)

Checks for uses of the builtin `eval()` function.

## [Why is this bad?](#why-is-this-bad)

The `eval()` function is insecure as it enables arbitrary code execution.

## [Example](#example)

```
def foo():
    x = eval(input("Enter a number: "))
    ...
```

Use instead:

```
def foo():
    x = input("Enter a number: ")
    ...
```

## [References](#references)

* [Python documentation: `eval`](https://docs.python.org/3/library/functions.html#eval)
* [*Eval really is dangerous* by Ned Batchelder](https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html)