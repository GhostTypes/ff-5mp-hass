# [too-many-public-methods (PLR0904)](#too-many-public-methods-plr0904)

Preview (since [v0.0.290](https://github.com/astral-sh/ruff/releases/tag/v0.0.290)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-public-methods%27%20OR%20PLR0904)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Ftoo_many_public_methods.rs#L85)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for classes with too many public methods

By default, this rule allows up to 20 public methods, as configured by
the [`lint.pylint.max-public-methods`](../../settings/#lint_pylint_max-public-methods) option.

## [Why is this bad?](#why-is-this-bad)

Classes with many public methods are harder to understand
and maintain.

Instead, consider refactoring the class into separate classes.

## [Example](#example)

Assuming that `lint.pylint.max-public-methods` is set to 5:

```
class Linter:
    def __init__(self):
        pass

    def pylint(self):
        pass

    def pylint_settings(self):
        pass

    def flake8(self):
        pass

    def flake8_settings(self):
        pass

    def pydocstyle(self):
        pass

    def pydocstyle_settings(self):
        pass
```

Use instead:

```
class Linter:
    def __init__(self):
        self.pylint = Pylint()
        self.flake8 = Flake8()
        self.pydocstyle = Pydocstyle()

    def lint(self):
        pass


class Pylint:
    def lint(self):
        pass

    def settings(self):
        pass


class Flake8:
    def lint(self):
        pass

    def settings(self):
        pass


class Pydocstyle:
    def lint(self):
        pass

    def settings(self):
        pass
```

## [Options](#options)

* [`lint.pylint.max-public-methods`](../../settings/#lint_pylint_max-public-methods)