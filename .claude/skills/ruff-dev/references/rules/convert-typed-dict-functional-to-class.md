# [convert-typed-dict-functional-to-class (UP013)](#convert-typed-dict-functional-to-class-up013)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27convert-typed-dict-functional-to-class%27%20OR%20UP013)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fconvert_typed_dict_functional_to_class.rs#L63)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `TypedDict` declarations that use functional syntax.

## [Why is this bad?](#why-is-this-bad)

`TypedDict` types can be defined either through a functional syntax
(`Foo = TypedDict(...)`) or a class syntax (`class Foo(TypedDict): ...`).

The class syntax is more readable and generally preferred over the
functional syntax.

Nonetheless, there are some situations in which it is impossible to use
the class-based syntax. This rule will not apply to those cases. Namely,
it is impossible to use the class-based syntax if any `TypedDict` fields are:

* Not valid [python identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) (for example, `@x`)
* [Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) such as `in`
* [Private names](https://docs.python.org/3/tutorial/classes.html#private-variables) such as `__id` that would undergo [name mangling](https://docs.python.org/3/reference/expressions.html#private-name-mangling) at runtime
  if the class-based syntax was used
* [Dunder names](https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers) such as `__int__` that can confuse type checkers if they're used
  with the class-based syntax.

## [Example](#example)

```
from typing import TypedDict

Foo = TypedDict("Foo", {"a": int, "b": str})
```

Use instead:

```
from typing import TypedDict


class Foo(TypedDict):
    a: int
    b: str
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe if there are any comments within the
range of the `TypedDict` definition, as these will be dropped by the
autofix.

## [References](#references)

* [Python documentation: `typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict)