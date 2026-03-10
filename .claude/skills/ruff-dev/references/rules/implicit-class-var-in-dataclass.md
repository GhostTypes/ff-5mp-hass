# [implicit-class-var-in-dataclass (RUF045)](#implicit-class-var-in-dataclass-ruf045)

Preview (since [0.9.7](https://github.com/astral-sh/ruff/releases/tag/0.9.7)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27implicit-class-var-in-dataclass%27%20OR%20RUF045)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fruff%2Frules%2Fimplicit_classvar_in_dataclass.rs#L54)

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for implicit class variables in dataclasses.

Variables matching the [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx) are excluded
from this rule.

## [Why is this bad?](#why-is-this-bad)

Class variables are shared between all instances of that class.
In dataclasses, fields with no annotations at all
are implicitly considered class variables, and a `TypeError` is
raised if a user attempts to initialize an instance of the class
with this field.

```
@dataclass
class C:
    a = 1
    b: str = ""

C(a = 42)  # TypeError: C.__init__() got an unexpected keyword argument 'a'
```

## [Example](#example)

```
@dataclass
class C:
    a = 1
```

Use instead:

```
from typing import ClassVar


@dataclass
class C:
    a: ClassVar[int] = 1
```

## [Options](#options)

* [`lint.dummy-variable-rgx`](../../settings/#lint_dummy-variable-rgx)