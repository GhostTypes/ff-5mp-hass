# [blank-lines-top-level (E302)](#blank-lines-top-level-e302)

Preview (since [v0.2.2](https://github.com/astral-sh/ruff/releases/tag/v0.2.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blank-lines-top-level%27%20OR%20E302)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fblank_lines.rs#L118)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for missing blank lines between top level functions and classes.

## [Why is this bad?](#why-is-this-bad)

PEP 8 recommends exactly two blank lines between top level functions and classes.

The rule respects the [`lint.isort.lines-after-imports`](../../settings/#lint_isort_lines-after-imports) setting when
determining the required number of blank lines between top-level `import`
statements and function or class definitions for compatibility with isort.

## [Example](#example)

```
def func1():
    pass
def func2():
    pass
```

Use instead:

```
def func1():
    pass


def func2():
    pass
```

## [Typing stub files (`.pyi`)](#typing-stub-files-pyi)

The typing style guide recommends to not use blank lines between classes and functions except to group
them. That's why this rule is not enabled in typing stub files.

## [Options](#options)

* [`lint.isort.lines-after-imports`](../../settings/#lint_isort_lines-after-imports)

## [References](#references)

* [PEP 8: Blank Lines](https://peps.python.org/pep-0008/#blank-lines)
* [Flake 8 rule](https://www.flake8rules.com/rules/E302.html)
* [Typing Style Guide](https://typing.python.org/en/latest/guides/writing_stubs.html#blank-lines)