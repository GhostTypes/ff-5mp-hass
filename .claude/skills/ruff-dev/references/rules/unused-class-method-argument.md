# [unused-class-method-argument (ARG003)](#unused-class-method-argument-arg003)

Added in [v0.0.168](https://github.com/astral-sh/ruff/releases/tag/v0.0.168) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unused-class-method-argument%27%20OR%20ARG003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_unused_arguments%2Frules%2Funused_arguments.rs#L146)

Derived from the **[flake8-unused-arguments](../#flake8-unused-arguments-arg)** linter.

## [What it does](#what-it-does)

Checks for the presence of unused arguments in class method definitions.

## [Why is this bad?](#why-is-this-bad)

An argument that is defined but not used is likely a mistake, and should
be removed to avoid confusion.

If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
[`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) pattern.

This rule exempts methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override).
Removing a parameter from a subclass method (or changing a parameter's
name) may cause type checkers to complain about a violation of the Liskov
Substitution Principle if it means that the method now incompatibly
overrides a method defined on a superclass. Explicitly decorating an
overriding method with `@override` signals to Ruff that the method is
intended to override a superclass method and that a type checker will
enforce that it does so; Ruff therefore knows that it should not enforce
rules about unused arguments on such methods.

## [Example](#example)

```
class Class:
    @classmethod
    def foo(cls, arg1, arg2):
        print(arg1)
```

Use instead:

```
class Class:
    @classmethod
    def foo(cls, arg1):
        print(arg1)
```

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)