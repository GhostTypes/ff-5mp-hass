# [raise-within-try (TRY301)](#raise-within-try-try301)

Added in [v0.0.233](https://github.com/astral-sh/ruff/releases/tag/v0.0.233) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27raise-within-try%27%20OR%20TRY301)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ftryceratops%2Frules%2Fraise_within_try.rs#L52)

Derived from the **[tryceratops](../#tryceratops-try)** linter.

## [What it does](#what-it-does)

Checks for `raise` statements within `try` blocks. The only `raise`s
caught are those that throw exceptions caught by the `try` statement itself.

## [Why is this bad?](#why-is-this-bad)

Raising and catching exceptions within the same `try` block is redundant,
as the code can be refactored to avoid the `try` block entirely.

Alternatively, the `raise` can be moved within an inner function, making
the exception reusable across multiple call sites.

## [Example](#example)

```
def bar():
    pass


def foo():
    try:
        a = bar()
        if not a:
            raise ValueError
    except ValueError:
        raise
```

Use instead:

```
def bar():
    raise ValueError


def foo():
    try:
        a = bar()  # refactored `bar` to raise `ValueError`
    except ValueError:
        raise
```