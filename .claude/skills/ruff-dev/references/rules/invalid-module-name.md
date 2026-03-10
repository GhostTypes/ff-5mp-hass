# [invalid-module-name (N999)](#invalid-module-name-n999)

Added in [v0.0.248](https://github.com/astral-sh/ruff/releases/tag/v0.0.248) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27invalid-module-name%27%20OR%20N999)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpep8_naming%2Frules%2Finvalid_module_name.rs#L40)

Derived from the **[pep8-naming](../#pep8-naming-n)** linter.

## [What it does](#what-it-does)

Checks for module names that do not follow the `snake_case` naming
convention or are otherwise invalid.

## [Why is this bad?](#why-is-this-bad)

[PEP 8](https://peps.python.org/pep-0008/#package-and-module-names) recommends the use of the `snake_case` naming convention for
module names:

> Modules should have short, all-lowercase names. Underscores can be used in the
> module name if it improves readability. Python packages should also have short,
> all-lowercase names, although the use of underscores is discouraged.
>
> When an extension module written in C or C++ has an accompanying Python module that
> provides a higher level (e.g. more object-oriented) interface, the C/C++ module has
> a leading underscore (e.g. `_socket`).

Further, in order for Python modules to be importable, they must be valid
identifiers. As such, they cannot start with a digit, or collide with hard
keywords, like `import` or `class`.

## [Example](#example)

* Instead of `example-module-name` or `example module name`, use `example_module_name`.
* Instead of `ExampleModule`, use `example_module`.