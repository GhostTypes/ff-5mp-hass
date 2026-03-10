# [blank-lines-before-nested-definition (E306)](#blank-lines-before-nested-definition-e306)

Preview (since [v0.2.2](https://github.com/astral-sh/ruff/releases/tag/v0.2.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blank-lines-before-nested-definition%27%20OR%20E306)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fblank_lines.rs#L340)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for 1 blank line between nested function or class definitions.

## [Why is this bad?](#why-is-this-bad)

PEP 8 recommends using blank lines as follows:

* Two blank lines are expected between functions and classes
* One blank line is expected between methods of a class.

## [Example](#example)

```
def outer():
    def inner():
        pass
    def inner2():
        pass
```

Use instead:

```
def outer():
    def inner():
        pass

    def inner2():
        pass
```

## [Typing stub files (`.pyi`)](#typing-stub-files-pyi)

The typing style guide recommends to not use blank lines between classes and functions except to group
them. That's why this rule is not enabled in typing stub files.

## [References](#references)

* [PEP 8: Blank Lines](https://peps.python.org/pep-0008/#blank-lines)
* [Flake 8 rule](https://www.flake8rules.com/rules/E306.html)
* [Typing Style Guide](https://typing.python.org/en/latest/guides/writing_stubs.html#blank-lines)