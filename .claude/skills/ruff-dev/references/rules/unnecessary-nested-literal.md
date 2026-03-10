# [unnecessary-nested-literal (RUF041)](#unnecessary-nested-literal-ruf041)

Added in [0.10.0](https://github.com/astral-sh/ruff/releases/tag/0.10.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unnecessary-nested-literal%27%20OR%20RUF041)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Funnecessary_nested_literal.rs#L61)

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for unnecessary nested `Literal`.

## [Why is this bad?](#why-is-this-bad)

Prefer using a single `Literal`, which is equivalent and more concise.

Parameterization of literals by other literals is supported as an ergonomic
feature as proposed in [PEP 586], to enable patterns such as:

```
ReadOnlyMode         = Literal["r", "r+"]
WriteAndTruncateMode = Literal["w", "w+", "wt", "w+t"]
WriteNoTruncateMode  = Literal["r+", "r+t"]
AppendMode           = Literal["a", "a+", "at", "a+t"]

AllModes = Literal[ReadOnlyMode, WriteAndTruncateMode,
                  WriteNoTruncateMode, AppendMode]
```

As a consequence, type checkers also support nesting of literals
which is less readable than a flat `Literal`:

```
AllModes = Literal[Literal["r", "r+"], Literal["w", "w+", "wt", "w+t"],
                  Literal["r+", "r+t"], Literal["a", "a+", "at", "a+t"]]
```

## [Example](#example)

```
AllModes = Literal[
    Literal["r", "r+"],
    Literal["w", "w+", "wt", "w+t"],
    Literal["r+", "r+t"],
    Literal["a", "a+", "at", "a+t"],
]
```

Use instead:

```
AllModes = Literal[
    "r", "r+", "w", "w+", "wt", "w+t", "r+", "r+t", "a", "a+", "at", "a+t"
]
```

or assign the literal to a variable as in the first example.

## [Fix safety](#fix-safety)

The fix for this rule is marked as unsafe when the `Literal` slice is split
across multiple lines and some of the lines have trailing comments.

## [References](#references)

* [Typing documentation: Legal parameters for `Literal` at type check time](https://typing.python.org/en/latest/spec/literal.html#legal-parameters-for-literal-at-type-check-time)

[PEP 586](https://peps.python.org/pep-0586/)