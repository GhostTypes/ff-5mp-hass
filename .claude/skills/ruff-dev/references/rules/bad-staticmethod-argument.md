# [bad-staticmethod-argument (PLW0211)](#bad-staticmethod-argument-plw0211)

Added in [0.6.0](https://github.com/astral-sh/ruff/releases/tag/0.6.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27bad-staticmethod-argument%27%20OR%20PLW0211)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fbad_staticmethod_argument.rs#L39)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for static methods that use `self` or `cls` as their first argument.
This rule also applies to `__new__` methods, which are implicitly static.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-method-arguments) recommends the use of `self` and `cls` as the first arguments for
instance methods and class methods, respectively. Naming the first argument
of a static method as `self` or `cls` can be misleading, as static methods
do not receive an instance or class reference as their first argument.

## [Example](#example)

```
class Wolf:
    @staticmethod
    def eat(self):
        pass
```

Use instead:

```
class Wolf:
    @staticmethod
    def eat(sheep):
        pass
```