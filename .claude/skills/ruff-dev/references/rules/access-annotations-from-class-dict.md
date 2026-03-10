# [access-annotations-from-class-dict (RUF063)](#access-annotations-from-class-dict-ruf063)

Preview (since [0.12.1](https://github.com/astral-sh/ruff/releases/tag/0.12.1)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27access-annotations-from-class-dict%27%20OR%20RUF063)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Faccess_annotations_from_class_dict.rs#L76)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of `foo.__dict__.get("__annotations__")` or
`foo.__dict__["__annotations__"]` on Python 3.10+ and Python < 3.10 when
[typing-extensions](https://docs.astral.sh/ruff/settings/#lint_typing-extensions)
is enabled.

## [Why is this bad?](#why-is-this-bad)

Starting with Python 3.14, directly accessing `__annotations__` via
`foo.__dict__.get("__annotations__")` or `foo.__dict__["__annotations__"]`
will only return annotations if the class is defined under
`from __future__ import annotations`.

Therefore, it is better to use dedicated library functions like
`annotationlib.get_annotations` (Python 3.14+), `inspect.get_annotations`
(Python 3.10+), or `typing_extensions.get_annotations` (for Python < 3.10 if
[typing-extensions](https://pypi.org/project/typing-extensions/) is
available).

The benefits of using these functions include:

1. **Avoiding Undocumented Internals:** They provide a stable, public API,
   unlike direct `__dict__` access which relies on implementation details.
2. **Forward-Compatibility:** They are designed to handle changes in
   Python's annotation system across versions, ensuring your code remains
   robust (e.g., correctly handling the Python 3.14 behavior mentioned
   above).

See [Python Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html)
for alternatives.

## [Example](#example)

```
foo.__dict__.get("__annotations__", {})
# or
foo.__dict__["__annotations__"]
```

On Python 3.14+, use instead:

```
import annotationlib

annotationlib.get_annotations(foo)
```

On Python 3.10+, use instead:

```
import inspect

inspect.get_annotations(foo)
```

On Python < 3.10 with [typing-extensions](https://pypi.org/project/typing-extensions/)
installed, use instead:

```
import typing_extensions

typing_extensions.get_annotations(foo)
```

## [Fix safety](#fix-safety)

No autofix is currently provided for this rule.

## [Fix availability](#fix-availability)

No autofix is currently provided for this rule.

## [References](#references)

* [Python Annotations Best Practices](https://docs.python.org/3.14/howto/annotations.html)