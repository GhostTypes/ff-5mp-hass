# [ambiguous-variable-name (E741)](#ambiguous-variable-name-e741)

Added in [v0.0.34](https://github.com/astral-sh/ruff/releases/tag/v0.0.34) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27ambiguous-variable-name%27%20OR%20E741)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fambiguous_variable_name.rs#L35)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

## [What it does](#what-it-does)

Checks for the use of the characters 'l', 'O', or 'I' as variable names.

Note: This rule is automatically disabled for all stub files
(files with `.pyi` extensions). The rule has little relevance for authors
of stubs: a well-written stub should aim to faithfully represent the
interface of the equivalent .py file as it exists at runtime, including any
ambiguously named variables in the runtime module.

## [Why is this bad?](#why-is-this-bad)

In some fonts, these characters are indistinguishable from the
numerals one and zero. When tempted to use 'l', use 'L' instead.

## [Example](#example)

```
l = 0
O = 123
I = 42
```

Use instead:

```
L = 0
o = 123
i = 42
```