# [no-classmethod-decorator (PLR0202)](#no-classmethod-decorator-plr0202)

Preview (since [v0.1.7](https://github.com/astral-sh/ruff/releases/tag/v0.1.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-classmethod-decorator%27%20OR%20PLR0202)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fno_method_decorator.rs#L35)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for the use of a classmethod being made without the decorator.

## [Why is this bad?](#why-is-this-bad)

When it comes to consistency and readability, it's preferred to use the decorator.

## [Example](#example)

```
class Foo:
    def bar(cls): ...

    bar = classmethod(bar)
```

Use instead:

```
class Foo:
    @classmethod
    def bar(cls): ...
```