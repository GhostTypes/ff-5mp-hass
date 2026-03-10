# [invalid-first-argument-name-for-class-method (N804)](#invalid-first-argument-name-for-class-method-n804)

Added in [v0.0.77](https://github.com/astral-sh/ruff/releases/tag/v0.0.77) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-first-argument-name-for-class-method%27%20OR%20N804)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Finvalid_first_argument_name.rs#L132)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for class methods that use a name other than `cls` for their
first argument.

The method `__new__` is exempted from this
check and the corresponding violation is caught by
[`bad-staticmethod-argument`](https://docs.astral.sh/ruff/rules/bad-staticmethod-argument/).

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#function-and-method-arguments) recommends the use of `cls` as the first argument for all class
methods:

> Always use `cls` for the first argument to class methods.
>
> If a function argument’s name clashes with a reserved keyword, it is generally better to
> append a single trailing underscore rather than use an abbreviation or spelling corruption.
> Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

Names can be excluded from this rule using the [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
or [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names) configuration options. For example,
to allow the use of `klass` as the first argument to class methods, set
the [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names) option to `["klass"]`.

## [Example](#example)

```
class Example:
    @classmethod
    def function(self, data): ...
```

Use instead:

```
class Example:
    @classmethod
    def function(cls, data): ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe, as renaming a method parameter
can change the behavior of the program.

## [Options](#options)

* [`lint.pep8-naming.classmethod-decorators`](../../settings/#lint_pep8-naming_classmethod-decorators)
* [`lint.pep8-naming.staticmethod-decorators`](../../settings/#lint_pep8-naming_staticmethod-decorators)
* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)