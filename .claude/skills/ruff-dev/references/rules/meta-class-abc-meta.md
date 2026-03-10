# [meta-class-abc-meta (FURB180)](#meta-class-abc-meta-furb180)

Preview (since [v0.2.0](https://github.com/astral-sh/ruff/releases/tag/v0.2.0)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27meta-class-abc-meta%27%20OR%20FURB180)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fmetaclass_abcmeta.rs#L49)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for uses of `metaclass=abc.ABCMeta` to define abstract base classes
(ABCs).

## [Why is this bad?](#why-is-this-bad)

Instead of `class C(metaclass=abc.ABCMeta): ...`, use `class C(ABC): ...`
to define an abstract base class. Inheriting from the `ABC` wrapper class
is semantically identical to setting `metaclass=abc.ABCMeta`, but more
succinct.

## [Example](#example)

```
import abc


class C(metaclass=abc.ABCMeta):
    pass
```

Use instead:

```
import abc


class C(abc.ABC):
    pass
```

## [Fix safety](#fix-safety)

The rule's fix is unsafe if the class has base classes. This is because the base classes might
be validating the class's other base classes (e.g., `typing.Protocol` does this) or otherwise
alter runtime behavior if more base classes are added.

## [References](#references)

* [Python documentation: `abc.ABC`](https://docs.python.org/3/library/abc.html#abc.ABC)
* [Python documentation: `abc.ABCMeta`](https://docs.python.org/3/library/abc.html#abc.ABCMeta)