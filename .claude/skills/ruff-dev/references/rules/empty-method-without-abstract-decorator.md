# [empty-method-without-abstract-decorator (B027)](#empty-method-without-abstract-decorator-b027)

Added in [v0.0.118](https://github.com/astral-sh/ruff/releases/tag/v0.0.118) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27empty-method-without-abstract-decorator%27%20OR%20B027)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fflake8_bugbear%2Frules%2Fabstract_base_class.rs#L102)

Derived from the **[flake8-bugbear](../#flake8-bugbear-b)** linter.

## [What it does](#what-it-does)

Checks for empty methods in abstract base classes without an abstract
decorator.

## [Why is this bad?](#why-is-this-bad)

Empty methods in abstract base classes without an abstract decorator may be
be indicative of a mistake. If the method is meant to be abstract, add an
`@abstractmethod` decorator to the method.

## [Example](#example)

```
from abc import ABC


class Foo(ABC):
    def method(self): ...
```

Use instead:

```
from abc import ABC, abstractmethod


class Foo(ABC):
    @abstractmethod
    def method(self): ...
```

## [References](#references)

* [Python documentation: `abc`](https://docs.python.org/3/library/abc.html)