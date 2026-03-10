# [duplicate-class-field-definition (PIE794)](#duplicate-class-field-definition-pie794)

Added in [v0.0.208](https://github.com/astral-sh/ruff/releases/tag/v0.0.208) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27duplicate-class-field-definition%27%20OR%20PIE794)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pie%2Frules%2Fduplicate_class_field_definition.rs#L37)

Derived from the **[flake8-pie](../#flake8-pie-pie)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for duplicate field definitions in classes.

## [Why is this bad?](#why-is-this-bad)

Defining a field multiple times in a class body is redundant and likely a
mistake.

## [Example](#example)

```
class Person:
    name = Tom
    ...
    name = Ben
```

Use instead:

```
class Person:
    name = Tom
    ...
```

## [Fix safety](#fix-safety)

This fix is always marked as unsafe since we cannot know
for certain which assignment was intended.