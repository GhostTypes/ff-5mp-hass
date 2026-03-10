# [django-unordered-body-content-in-model (DJ012)](#django-unordered-body-content-in-model-dj012)

Added in [v0.0.258](https://github.com/astral-sh/ruff/releases/tag/v0.0.258) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-unordered-body-content-in-model%27%20OR%20DJ012)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Funordered_body_content_in_model.rs#L65)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks for the order of Model's inner classes, methods, and fields as per
the [Django Style Guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style).

## [Why is this bad?](#why-is-this-bad)

The [Django Style Guide](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style) specifies that the order of Model inner classes,
attributes and methods should be as follows:

1. All database fields
2. Custom manager attributes
3. `class Meta`
4. `def __str__()`
5. `def save()`
6. `def get_absolute_url()`
7. Any custom methods

## [Example](#example)

```
from django.db import models


class StrBeforeFieldModel(models.Model):
    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

    def __str__(self):
        return "foobar"

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=40)
```

Use instead:

```
from django.db import models


class StrBeforeFieldModel(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

    def __str__(self):
        return "foobar"
```