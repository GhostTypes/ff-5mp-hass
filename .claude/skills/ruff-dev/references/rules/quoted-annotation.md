# [quoted-annotation (UP037)](#quoted-annotation-up037)

Added in [v0.0.242](https://github.com/astral-sh/ruff/releases/tag/v0.0.242) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27quoted-annotation%27%20OR%20UP037)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fquoted_annotation.rs#L89)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for the presence of unnecessary quotes in type annotations.

## [Why is this bad?](#why-is-this-bad)

In Python, type annotations can be quoted to avoid forward references.

However, if `from __future__ import annotations` is present, Python
will always evaluate type annotations in a deferred manner, making
the quotes unnecessary.

Similarly, if the annotation is located in a typing-only context and
won't be evaluated by Python at runtime, the quotes will also be
considered unnecessary. For example, Python does not evaluate type
annotations on assignments in function bodies.

## [Example](#example)

Given:

```
from __future__ import annotations


def foo(bar: "Bar") -> "Bar": ...
```

Use instead:

```
from __future__ import annotations


def foo(bar: Bar) -> Bar: ...
```

Given:

```
def foo() -> None:
    bar: "Bar"
```

Use instead:

```
def foo() -> None:
    bar: Bar
```

## [Preview](#preview)

When [preview](https://docs.astral.sh/ruff/preview/) is enabled, if [`lint.future-annotations`](../../settings/#lint_future-annotations) is set to `true`,
`from __future__ import annotations` will be added if doing so would allow an annotation to be
unquoted.

## [Fix safety](#fix-safety)

The rule's fix is marked as safe, unless [preview](https://docs.astral.sh/ruff/preview/) and
[`lint.future-annotations`](../../settings/#lint_future-annotations) are enabled and a `from __future__ import annotations` import is added. Such an import may change the behavior of all annotations in the
file.

## [Options](#options)

* [`lint.future-annotations`](../../settings/#lint_future-annotations)

## [See also](#see-also)

* [`quoted-annotation-in-stub`](https://docs.astral.sh/ruff/rules/quoted-annotation-in-stub/): A rule that
  removes all quoted annotations from stub files
* [`quoted-type-alias`](https://docs.astral.sh/ruff/rules/quoted-type-alias/): A rule that removes unnecessary quotes
  from type aliases.

## [References](#references)

* [PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)
* [Python documentation: `__future__`](https://docs.python.org/3/library/__future__.html#module-__future__)