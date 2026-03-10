# [blank-line-after-decorator (E304)](#blank-line-after-decorator-e304)

Preview (since [v0.2.2](https://github.com/astral-sh/ruff/releases/tag/v0.2.2)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27blank-line-after-decorator%27%20OR%20E304)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpycodestyle%2Frules%2Fblank_lines.rs#L233)

Derived from the **[pycodestyle](../#pycodestyle-e-w)** linter.

Fix is always available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for extraneous blank line(s) after function decorators.

## [Why is this bad?](#why-is-this-bad)

There should be no blank lines between a decorator and the object it is decorating.

## [Example](#example)

```
class User(object):

    @property

    def name(self):
        pass
```

Use instead:

```
class User(object):

    @property
    def name(self):
        pass
```

## [References](#references)

* [PEP 8: Blank Lines](https://peps.python.org/pep-0008/#blank-lines)
* [Flake 8 rule](https://www.flake8rules.com/rules/E304.html)