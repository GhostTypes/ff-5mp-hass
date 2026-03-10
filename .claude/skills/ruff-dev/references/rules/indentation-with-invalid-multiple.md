# [indentation-with-invalid-multiple (E111)](#indentation-with-invalid-multiple-e111)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27indentation-with-invalid-multiple%27%20OR%20E111)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Findentation.rs#L40)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for indentation with a non-multiple of 4 spaces.

## [Why is this bad?](#why-is-this-bad)

According to [PEP 8](https://peps.python.org/pep-0008/#indentation), 4 spaces per indentation level should be preferred.

## [Example](#example)

```
if True:
   a = 1
```

Use instead:

```
if True:
    a = 1
```

## [Formatter compatibility](#formatter-compatibility)

We recommend against using this rule alongside the [formatter](https://docs.astral.sh/ruff/formatter/). The
formatter enforces consistent indentation, making the rule redundant.

The rule is also incompatible with the [formatter](https://docs.astral.sh/ruff/formatter/) when using
`indent-width` with a value other than `4`.

## [Options](#options)

* [`indent-width`](../../settings/#indent-width)