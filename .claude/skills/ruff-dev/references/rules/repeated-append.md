# [repeated-append (FURB113)](#repeated-append-furb113)

Preview (since [v0.0.287](https://github.com/astral-sh/ruff/releases/tag/v0.0.287)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27repeated-append%27%20OR%20FURB113)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Frepeated_append.rs#L47)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for consecutive calls to `append`.

## [Why is this bad?](#why-is-this-bad)

Consecutive calls to `append` can be less efficient than batching them into
a single `extend`. Each `append` resizes the list individually, whereas an
`extend` can resize the list once for all elements.

## [Known problems](#known-problems)

This rule is prone to false negatives due to type inference limitations,
as it will only detect lists that are instantiated as literals or annotated
with a type annotation.

## [Example](#example)

```
nums = [1, 2, 3]

nums.append(4)
nums.append(5)
nums.append(6)
```

Use instead:

```
nums = [1, 2, 3]

nums.extend((4, 5, 6))
```

## [References](#references)

* [Python documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)