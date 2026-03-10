# [multiple-leading-hashes-for-block-comment (E266)](#multiple-leading-hashes-for-block-comment-e266)

Preview (since [v0.0.269](https://github.com/astral-sh/ruff/releases/tag/v0.0.269)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27multiple-leading-hashes-for-block-comment%27%20OR%20E266)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Flogical_lines%2Fwhitespace_before_comment.rs#L155)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for block comments that start with multiple leading `#` characters.

## [Why is this bad?](#why-is-this-bad)

Per [PEP 8](https://peps.python.org/pep-0008/#comments), "Block comments generally consist of one or more paragraphs built
out of complete sentences, with each sentence ending in a period."

Each line of a block comment should start with a `#` followed by a single space.

Shebangs (lines starting with `#!`, at the top of a file) are exempt from this
rule.

## [Example](#example)

```
### Block comment
```

Use instead:

```
# Block comment
```

Alternatively, this rule makes an exception for comments that consist
solely of `#` characters, as in:

```
##############
# Block header
##############
```