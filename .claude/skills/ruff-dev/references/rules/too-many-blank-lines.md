# [too-many-blank-lines (E303)](#too-many-blank-lines-e303)

Preview (since [v0.2.2](https://github.com/astral-sh/ruff/releases/tag/v0.2.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27too-many-blank-lines%27%20OR%20E303)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fblank_lines.rs#L186)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous blank lines.

## [Why is this bad?](#why-is-this-bad)

PEP 8 recommends using blank lines as follows:

* No more than two blank lines between top-level statements.
* No more than one blank line between non-top-level statements.

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

The rule allows at most one blank line in typing stub files in accordance to the typing style guide recommendation.

Note: The rule respects the following `isort` settings when determining the maximum number of blank lines allowed between two statements:

* [`lint.isort.lines-after-imports`](../../settings/#lint_isort_lines-after-imports): For top-level statements directly following an import statement.
* [`lint.isort.lines-between-types`](../../settings/#lint_isort_lines-between-types): For `import` statements directly following a `from ... import ...` statement or vice versa.

## [Options](#options)

* [`lint.isort.lines-after-imports`](../../settings/#lint_isort_lines-after-imports)
* [`lint.isort.lines-between-types`](../../settings/#lint_isort_lines-between-types)

## [References](#references)

* [PEP 8: Blank Lines](https://peps.python.org/pep-0008/#blank-lines)
* [Flake 8 rule](https://www.flake8rules.com/rules/E303.html)
* [Typing Style Guide](https://typing.python.org/en/latest/guides/writing_stubs.html#blank-lines)