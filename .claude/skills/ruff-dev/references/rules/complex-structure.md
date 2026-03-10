# [complex-structure (C901)](#complex-structure-c901)

Added in [v0.0.127](https://github.com/astral-sh/ruff/releases/tag/v0.0.127) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27complex-structure%27%20OR%20C901)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fmccabe%2Frules%2Ffunction_is_too_complex.rs#L50)

Derived from the **[mccabe](../#mccabe-c90)** linter.

## [What it does](#what-it-does)

Checks for functions with a high `McCabe` complexity.

## [Why is this bad?](#why-is-this-bad)

The `McCabe` complexity of a function is a measure of the complexity of
the control flow graph of the function. It is calculated by adding
one to the number of decision points in the function. A decision
point is a place in the code where the program has a choice of two
or more paths to follow.

Functions with a high complexity are hard to understand and maintain.

## [Example](#example)

```
def foo(a, b, c):
    if a:
        if b:
            if c:
                return 1
            else:
                return 2
        else:
            return 3
    else:
        return 4
```

Use instead:

```
def foo(a, b, c):
    if not a:
        return 4
    if not b:
        return 3
    if not c:
        return 2
    return 1
```

## [Options](#options)

* [`lint.mccabe.max-complexity`](../../settings/#lint_mccabe_max-complexity)