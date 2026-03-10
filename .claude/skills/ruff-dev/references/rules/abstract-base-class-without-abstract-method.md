# [abstract-base-class-without-abstract-method (B024)](#abstract-base-class-without-abstract-method-b024)

Added in [v0.0.118](https://github.com/astral-sh/ruff/releases/tag/v0.0.118) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27abstract-base-class-without-abstract-method%27%20OR%20B024)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fabstract_base_class.rs#L56)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for abstract classes without abstract methods or properties.
Annotated but unassigned class variables are regarded as abstract.

## [Why is this bad?](#why-is-this-bad)

Abstract base classes are used to define interfaces. If an abstract base
class has no abstract methods or properties, you may have forgotten
to add an abstract method or property to the class,
or omitted an `@abstractmethod` decorator.

If the class is *not* meant to be used as an interface, consider removing
the `ABC` base class from the class definition.

## [Example](#example)

```
from abc import ABC
from typing import ClassVar


class Foo(ABC):
    class_var: ClassVar[str] = "assigned"

    def method(self):
        bar()
```

Use instead:

```
from abc import ABC, abstractmethod
from typing import ClassVar


class Foo(ABC):
    class_var: ClassVar[str]  # unassigned

    @abstractmethod
    def method(self):
        bar()
```

## [References](#references)

* [Python documentation: `abc`](https://docs.python.org/3/library/abc.html)
* [Python documentation: `typing.ClassVar`](https://docs.python.org/3/library/typing.html#typing.ClassVar)