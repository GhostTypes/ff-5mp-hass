# [empty-comment (PLR2044)](#empty-comment-plr2044)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27empty-comment%27%20OR%20PLR2044)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fempty_comment.rs#L32)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for a # symbol appearing on a line not followed by an actual comment.

## [Why is this bad?](#why-is-this-bad)

Empty comments don't provide any clarity to the code, and just add clutter.
Either add a comment or delete the empty comment.

## [Example](#example)

```
class Foo:  #
    pass
```

Use instead:

```
class Foo:
    pass
```

## [References](#references)

* [Pylint documentation](https://pylint.pycqa.org/en/latest/user_guide/messages/refactor/empty-comment.html)