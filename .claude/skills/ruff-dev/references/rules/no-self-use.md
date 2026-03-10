# [no-self-use (PLR6301)](#no-self-use-plr6301)

Preview (since [v0.0.286](https://github.com/astral-sh/ruff/releases/tag/v0.0.286)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27no-self-use%27%20OR%20PLR6301)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fno_self_use.rs#L53)

Derived from the **[Pylint](../#pylint-pl)** linter.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for the presence of unused `self` parameter in methods definitions.

## [Why is this bad?](#why-is-this-bad)

Unused `self` parameters are usually a sign of a method that could be
replaced by a function, class method, or static method.

This rule exempts methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override).
Converting an instance method into a static method or class method may
cause type checkers to complain about a violation of the Liskov
Substitution Principle if it means that the method now incompatibly
overrides a method defined on a superclass. Explicitly decorating an
overriding method with `@override` signals to Ruff that the method is
intended to override a superclass method and that a type checker will
enforce that it does so; Ruff therefore knows that it should not enforce
rules about unused `self` parameters on such methods.

## [Example](#example)

```
class Person:
    def greeting(self):
        print("Greetings friend!")
```

Use instead:

```
def greeting():
    print("Greetings friend!")
```

or

```
class Person:
    @staticmethod
    def greeting():
        print("Greetings friend!")
```