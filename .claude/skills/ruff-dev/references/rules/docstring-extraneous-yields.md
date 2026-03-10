# [docstring-extraneous-yields (DOC403)](#docstring-extraneous-yields-doc403)

Preview (since [0.5.7](https://github.com/astral-sh/ruff/releases/tag/0.5.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27docstring-extraneous-yields%27%20OR%20DOC403)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydoclint%2Frules%2Fcheck_docstring.rs#L273)

Derived from the **[pydoclint](../#pydoclint-doc)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for function docstrings with unnecessary "Yields" sections.

## [Why is this bad?](#why-is-this-bad)

A function that doesn't yield anything should not have a "Yields" section
in its docstring.

This rule is not enforced for abstract methods. It is also ignored for
"stub functions": functions where the body only consists of `pass`, `...`,
`raise NotImplementedError`, or similar.

## [Example](#example)

```
def say_hello(n: int) -> None:
    """Says hello to the user.

    Args:
        n: Number of times to say hello.

    Yields:
        Doesn't yield anything.
    """
    for _ in range(n):
        print("Hello!")
```

Use instead:

```
def say_hello(n: int) -> None:
    """Says hello to the user.

    Args:
        n: Number of times to say hello.
    """
    for _ in range(n):
        print("Hello!")
```