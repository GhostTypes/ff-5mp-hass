# [non-self-return-type (PYI034)](#non-self-return-type-pyi034)

Added in [v0.0.271](https://github.com/astral-sh/ruff/releases/tag/v0.0.271) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27non-self-return-type%27%20OR%20PYI034)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fnon_self_return_type.rs#L115)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for methods that are annotated with a fixed return type which
should instead be returning `Self`.

## [Why is this bad?](#why-is-this-bad)

If methods that generally return `self` at runtime are annotated with a
fixed return type, and the class is subclassed, type checkers will not be
able to infer the correct return type.

For example:

```
class Shape:
    def set_scale(self, scale: float) -> Shape:
        self.scale = scale
        return self

class Circle(Shape):
    def set_radius(self, radius: float) -> Circle:
        self.radius = radius
        return self

# Type checker infers return type as `Shape`, not `Circle`.
Circle().set_scale(0.5)

# Thus, this expression is invalid, as `Shape` has no attribute `set_radius`.
Circle().set_scale(0.5).set_radius(2.7)
```

Specifically, this check enforces that the return type of the following
methods is `Self`:

1. In-place binary-operation dunder methods, like `__iadd__`, `__imul__`, etc.
2. `__new__`, `__enter__`, and `__aenter__`, if those methods return the
   class name.
3. `__iter__` methods that return `Iterator`, despite the class inheriting
   directly from `Iterator`.
4. `__aiter__` methods that return `AsyncIterator`, despite the class
   inheriting directly from `AsyncIterator`.

The rule attempts to avoid flagging methods on metaclasses, since
[PEP 673](https://peps.python.org/pep-0673/#valid-locations-for-self) specifies that `Self` is disallowed in metaclasses. Ruff can
detect a class as being a metaclass if it inherits from a stdlib
metaclass such as `builtins.type` or `abc.ABCMeta`, and additionally
infers that a class may be a metaclass if it has a `__new__` method
with a similar signature to `type.__new__`. The heuristic used to
identify a metaclass-like `__new__` method signature is that it:

1. Has exactly 5 parameters (including `cls`)
2. Has a second parameter annotated with `str`
3. Has a third parameter annotated with a `tuple` type
4. Has a fourth parameter annotated with a `dict` type
5. Has a fifth parameter is keyword-variadic (`**kwargs`)

For example, the following class would be detected as a metaclass, disabling
the rule:

```
class MyMetaclass(django.db.models.base.ModelBase):
    def __new__(cls, name: str, bases: tuple[Any, ...], attrs: dict[str, Any], **kwargs: Any) -> MyMetaclass:
        ...
```

## [Example](#example)

```
class Foo:
    def __new__(cls, *args: Any, **kwargs: Any) -> Foo: ...
    def __enter__(self) -> Foo: ...
    async def __aenter__(self) -> Foo: ...
    def __iadd__(self, other: Foo) -> Foo: ...
```

Use instead:

```
from typing_extensions import Self

class Foo:
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def __enter__(self) -> Self: ...
    async def __aenter__(self) -> Self: ...
    def __iadd__(self, other: Foo) -> Self: ...
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe as it changes the meaning of your type annotations.

## [Availability](#availability)

Because this rule relies on the third-party `typing_extensions` module for Python versions
before 3.11, its diagnostic will not be emitted, and no fix will be offered, if
`typing_extensions` imports have been disabled by the [`lint.typing-extensions`](../../settings/#lint_typing-extensions) linter option.

## [Options](#options)

* [`lint.typing-extensions`](../../settings/#lint_typing-extensions)

## [References](#references)

* [Python documentation: `typing.Self`](https://docs.python.org/3/library/typing.html#typing.Self)