# [django-non-leading-receiver-decorator (DJ013)](#django-non-leading-receiver-decorator-dj013)

Added in [v0.0.246](https://github.com/astral-sh/ruff/releases/tag/v0.0.246) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27django-non-leading-receiver-decorator%27%20OR%20DJ013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_django%2Frules%2Fnon_leading_receiver_decorator.rs#L43)

Derived from the **[flake8-django](../#flake8-django-dj)** linter.

## [What it does](#what-it-does)

Checks that Django's `@receiver` decorator is listed first, prior to
any other decorators.

## [Why is this bad?](#why-is-this-bad)

Django's `@receiver` decorator is special in that it does not return
a wrapped function. Rather, `@receiver` connects the decorated function
to a signal. If any other decorators are listed before `@receiver`,
the decorated function will not be connected to the signal.

## [Example](#example)

```
from django.dispatch import receiver
from django.db.models.signals import post_save


@transaction.atomic
@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    pass
```

Use instead:

```
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=MyModel)
@transaction.atomic
def my_handler(sender, instance, created, **kwargs):
    pass
```