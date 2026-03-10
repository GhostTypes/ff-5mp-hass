# [django-all-with-model-form (DJ007)](#django-all-with-model-form-dj007)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-all-with-model-form%27%20OR%20DJ007)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Fall_with_model_form.rs#L40)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks for the use of `fields = "__all__"` in Django `ModelForm`
classes.

## [Why is this bad?](#why-is-this-bad)

If a `ModelForm` includes the `fields = "__all__"` attribute, any new
field that is added to the model will automatically be exposed for
modification.

## [Example](#example)

```
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
```

Use instead:

```
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
```