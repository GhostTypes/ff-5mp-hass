# [django-locals-in-render-function (DJ003)](#django-locals-in-render-function-dj003)

Added in [v0.0.253](https://github.com/astral-sh/ruff/releases/tag/v0.0.253) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-locals-in-render-function%27%20OR%20DJ003)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Flocals_in_render_function.rs#L36)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks for the use of `locals()` in `render` functions.

## [Why is this bad?](#why-is-this-bad)

Using `locals()` can expose internal variables or other unintentional
data to the rendered template.

## [Example](#example)

```
from django.shortcuts import render


def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", locals())
```

Use instead:

```
from django.shortcuts import render


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "app/index.html", context)
```