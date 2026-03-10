# [loop-iterator-mutation (B909)](#loop-iterator-mutation-b909)

Preview (since [v0.3.7](https://github.com/astral-sh/ruff/releases/tag/v0.3.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27loop-iterator-mutation%27%20OR%20B909)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Floop_iterator_mutation.rs#L38)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for mutations to an iterable during a loop iteration.

## [Why is this bad?](#why-is-this-bad)

When iterating over an iterable, mutating the iterable can lead to unexpected
behavior, like skipping elements or infinite loops.

## [Example](#example)

```
items = [1, 2, 3]

for item in items:
    print(item)

    # Create an infinite loop by appending to the list.
    items.append(item)
```

## [References](#references)

* [Python documentation: Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)