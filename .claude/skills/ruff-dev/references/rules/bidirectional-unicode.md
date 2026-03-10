# [bidirectional-unicode (PLE2502)](#bidirectional-unicode-ple2502)

Added in [v0.0.244](https://github.com/astral-sh/ruff/releases/tag/v0.0.244) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bidirectional-unicode%27%20OR%20PLE2502)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbidirectional_unicode.rs#L52)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for bidirectional formatting characters.

## [Why is this bad?](#why-is-this-bad)

The interaction between bidirectional formatting characters and the
surrounding code can be surprising to those that are unfamiliar
with right-to-left writing systems.

In some cases, bidirectional formatting characters can also be used to
obfuscate code and introduce or mask security vulnerabilities.

## [Example](#example)

```
example = "x‏" * 100  #    "‏x" is assigned
```

The example uses two `RIGHT-TO-LEFT MARK`s to make the `100 *` appear inside the comment.
Without the `RIGHT-TO-LEFT MARK`s, the code looks like this:

```
example = "x" * 100  #    "x" is assigned
```

## [References](#references)

* [PEP 672: Bidirectional Marks, Embeddings, Overrides and Isolates](https://peps.python.org/pep-0672/#bidirectional-marks-embeddings-overrides-and-isolates)