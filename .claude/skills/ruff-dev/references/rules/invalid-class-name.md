# [invalid-class-name (N801)](#invalid-class-name-n801)

Added in [v0.0.77](https://github.com/astral-sh/ruff/releases/tag/v0.0.77) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-class-name%27%20OR%20N801)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Finvalid_class_name.rs#L43)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for class names that do not follow the `CamelCase` convention.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#class-names) recommends the use of the `CapWords` (or `CamelCase`) convention
for class names:

> Class names should normally use the `CapWords` convention.
>
> The naming convention for functions may be used instead in cases where the interface is
> documented and used primarily as a callable.
>
> Note that there is a separate convention for builtin names: most builtin names are single
> words (or two words run together), with the `CapWords` convention used only for exception
> names and builtin constants.

## [Example](#example)

```
class my_class:
    pass
```

Use instead:

```
class MyClass:
    pass
```

## [Options](#options)

* [`lint.pep8-naming.ignore-names`](../../settings/#lint_pep8-naming_ignore-names)
* [`lint.pep8-naming.extend-ignore-names`](../../settings/#lint_pep8-naming_extend-ignore-names)