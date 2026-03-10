# [django-nullable-model-string-field (DJ001)](#django-nullable-model-string-field-dj001)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-nullable-model-string-field%27%20OR%20DJ001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Fnullable_model_string_field.rs#L43)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks nullable string-based fields (like `CharField` and `TextField`)
in Django models.

## [Why is this bad?](#why-is-this-bad)

If a string-based field is nullable, then your model will have two possible
representations for "no data": `None` and the empty string. This can lead to
confusion, as clients of the API have to check for both `None` and the
empty string when trying to determine if the field has data.

The Django convention is to use the empty string in lieu of `None` for
string-based fields.

## [Example](#example)

```
from django.db import models


class MyModel(models.Model):
    field = models.CharField(max_length=255, null=True)
```

Use instead:

```
from django.db import models


class MyModel(models.Model):
    field = models.CharField(max_length=255, default="")
```