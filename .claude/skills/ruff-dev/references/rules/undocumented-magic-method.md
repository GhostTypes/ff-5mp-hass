# [undocumented-magic-method (D105)](#undocumented-magic-method-d105)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-magic-method%27%20OR%20D105)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnot_missing.rs#L432)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for undocumented magic method definitions.

## [Why is this bad?](#why-is-this-bad)

Magic methods (methods with names that start and end with double
underscores) are used to implement operator overloading and other special
behavior. Such methods should be documented via docstrings to
outline their behavior.

Generally, magic method docstrings should describe the method's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.

If the codebase adheres to a standard format for method docstrings, follow
that format for consistency.

## [Example](#example)

```
class Cat(Animal):
    def __str__(self) -> str:
        return f"Cat: {self.name}"


cat = Cat("Dusty")
print(cat)  # "Cat: Dusty"
```

Use instead:

```
class Cat(Animal):
    def __str__(self) -> str:
        """Return a string representation of the cat."""
        return f"Cat: {self.name}"


cat = Cat("Dusty")
print(cat)  # "Cat: Dusty"
```

## [Options](#options)

* [`lint.pydocstyle.ignore-decorators`](../../settings/#lint_pydocstyle_ignore-decorators)

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)