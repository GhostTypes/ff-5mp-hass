# [undocumented-public-method (D102)](#undocumented-public-method-d102)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-public-method%27%20OR%20D102)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnot_missing.rs#L239)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for undocumented public method definitions.

## [Why is this bad?](#why-is-this-bad)

Public methods should be documented via docstrings to outline their purpose
and behavior.

Generally, a method docstring should describe the method's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.

If the codebase adheres to a standard format for method docstrings, follow
that format for consistency.

This rule exempts methods decorated with [`@typing.override`](https://docs.python.org/3/library/typing.html#typing.override),
since it is a common practice to document a method on a superclass but not
on an overriding method in a subclass.

## [Example](#example)

```
class Cat(Animal):
    def greet(self, happy: bool = True):
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
```

Use instead (in the NumPy docstring format):

```
class Cat(Animal):
    def greet(self, happy: bool = True):
        """Print a greeting from the cat.

        Parameters
        ----------
        happy : bool, optional
            Whether the cat is happy, is True by default.

        Raises
        ------
        ValueError
            If the cat is not happy.
        """
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
```

Or (in the Google docstring format):

```
class Cat(Animal):
    def greet(self, happy: bool = True):
        """Print a greeting from the cat.

        Args:
            happy: Whether the cat is happy, is True by default.

        Raises:
            ValueError: If the cat is not happy.
        """
        if happy:
            print("Meow!")
        else:
            raise ValueError("Tried to greet an unhappy cat.")
```

## [Options](#options)

* [`lint.pydocstyle.ignore-decorators`](../../settings/#lint_pydocstyle_ignore-decorators)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)