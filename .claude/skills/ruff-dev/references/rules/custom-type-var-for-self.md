# [custom-type-var-for-self (PYI019)](#custom-type-var-for-self-pyi019)

Added in [v0.0.283](https://github.com/astral-sh/ruff/releases/tag/v0.0.283) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27custom-type-var-for-self%27%20OR%20PYI019)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_pyi%2Frules%2Fcustom_type_var_for_self.rs#L91)

Derived from the **[flake8-pyi](../#flake8-pyi-pyi)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for methods that use custom [`TypeVar`s](https://docs.python.org/3/library/typing.html#typing.TypeVar) in their
annotations when they could use [`Self`](https://docs.python.org/3/library/typing.html#typing.Self) instead.

## [Why is this bad?](#why-is-this-bad)

While the semantics are often identical, using `Self` is more intuitive
and succinct (per [PEP 673](https://peps.python.org/pep-0673/#motivation)) than a custom `TypeVar`. For example, the
use of `Self` will typically allow for the omission of type parameters
on the `self` and `cls` arguments.

This check currently applies to instance methods that return `self`,
class methods that return an instance of `cls`, class methods that return
`cls`, and `__new__` methods.

## [Example](#example)

```
from typing import TypeVar

_S = TypeVar("_S", bound="Foo")

class Foo:
    def __new__(cls: type[_S], *args: str, **kwargs: int) -> _S: ...
    def foo(self: _S, arg: bytes) -> _S: ...
    @classmethod
    def bar(cls: type[_S], arg: int) -> _S: ...
```

Use instead:

```
from typing import Self

class Foo:
    def __new__(cls, *args: str, **kwargs: int) -> Self: ...
    def foo(self, arg: bytes) -> Self: ...
    @classmethod
    def bar(cls, arg: int) -> Self: ...
```

## [Fix behaviour](#fix-behaviour)

The fix replaces all references to the custom type variable in the method's header and body
with references to `Self`. The fix also adds an import of `Self` if neither `Self` nor `typing`
is already imported in the module. If your [`target-version`](../../settings/#target-version) setting is set to Python 3.11 or
newer, the fix imports `Self` from the standard-library `typing` module; otherwise, the fix
imports `Self` from the third-party [`typing_extensions`](https://typing-extensions.readthedocs.io/en/latest/) backport package.

If the custom type variable is a [PEP-695](https://peps.python.org/pep-0695/)-style `TypeVar`, the fix also removes the `TypeVar`
declaration from the method's [type parameter list](https://docs.python.org/3/reference/compound_stmts.html#type-params). However, if the type variable is an
old-style `TypeVar`, the declaration of the type variable will not be removed by this rule's
fix, as the type variable could still be used by other functions, methods or classes. See
[`unused-private-type-var`](https://docs.astral.sh/ruff/rules/unused-private-type-var/) for a rule that will clean up unused private type
variables.

## [Fix safety](#fix-safety)

The fix is only marked as unsafe if there is the possibility that it might delete a comment
from your code.

## [Availability](#availability)

Because this rule relies on the third-party `typing_extensions` module for Python versions
before 3.11, its diagnostic will not be emitted, and no fix will be offered, if
`typing_extensions` imports have been disabled by the [`lint.typing-extensions`](../../settings/#lint_typing-extensions) linter option.

## [Options](#options)

* [`lint.typing-extensions`](../../settings/#lint_typing-extensions)