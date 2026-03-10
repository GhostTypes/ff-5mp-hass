# [django-model-without-dunder-str (DJ008)](#django-model-without-dunder-str-dj008)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-model-without-dunder-str%27%20OR%20DJ008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Fmodel_without_dunder_str.rs#L43)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks that a `__str__` method is defined in Django models.

## [Why is this bad?](#why-is-this-bad)

Django models should define a `__str__` method to return a string representation
of the model instance, as Django calls this method to display the object in
the Django Admin and elsewhere.

Models without a `__str__` method will display a non-meaningful representation
of the object in the Django Admin.

## [Example](#example)

```
from django.db import models


class MyModel(models.Model):
    field = models.CharField(max_length=255)
```

Use instead:

```
from django.db import models


class MyModel(models.Model):
    field = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.field}"
```