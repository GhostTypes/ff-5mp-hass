# [super-without-brackets (PLW0245)](#super-without-brackets-plw0245)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27super-without-brackets%27%20OR%20PLW0245)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fsuper_without_brackets.rs#L49)

Derived from the **[Pylint](../#pylint-pl)** linter.

Fix is always available.

## [What it does](#what-it-does)

Detects attempts to use `super` without parentheses.

## [Why is this bad?](#why-is-this-bad)

The [`super()` callable](https://docs.python.org/3/library/functions.html#super)
can be used inside method definitions to create a proxy object that
delegates attribute access to a superclass of the current class. Attempting
to access attributes on `super` itself, however, instead of the object
returned by a call to `super()`, will raise `AttributeError`.

## [Example](#example)

```
class Animal:
    @staticmethod
    def speak():
        return "This animal says something."


class Dog(Animal):
    @staticmethod
    def speak():
        original_speak = super.speak()  # ERROR: `super.speak()`
        return f"{original_speak} But as a dog, it barks!"
```

Use instead:

```
class Animal:
    @staticmethod
    def speak():
        return "This animal says something."


class Dog(Animal):
    @staticmethod
    def speak():
        original_speak = super().speak()  # Correct: `super().speak()`
        return f"{original_speak} But as a dog, it barks!"
```