# [import-outside-top-level (PLC0415)](#import-outside-top-level-plc0415)

Added in [0.12.0](https://github.com/astral-sh/ruff/releases/tag/0.12.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27import-outside-top-level%27%20OR%20PLC0415)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Fimport_outside_top_level.rs#L55)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for `import` statements outside of a module's top-level scope, such
as within a function or class definition.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#imports) recommends placing imports not only at the top-level of a module,
but at the very top of the file, "just after any module comments and
docstrings, and before module globals and constants."

`import` statements have effects that are global in scope; defining them at
the top level has a number of benefits. For example, it makes it easier to
identify the dependencies of a module, and ensures that any invalid imports
are caught regardless of whether a specific function is called or class is
instantiated.

An import statement would typically be placed within a function only to
avoid a circular dependency, to defer a costly module load, or to avoid
loading a dependency altogether in a certain runtime environment.

## [Example](#example)

```
def print_python_version():
    import platform

    print(platform.python_version())
```

Use instead:

```
import platform


def print_python_version():
    print(platform.python_version())
```

## [See also](#see-also)

This rule will ignore import statements configured in
[`lint.flake8-tidy-imports.banned-module-level-imports`](https://docs.astral.sh/ruff/settings/#lint_flake8-tidy-imports_banned-module-level-imports)
if the rule [`banned-module-level-imports`](https://docs.astral.sh/ruff/rules/banned-module-level-imports/) is enabled.