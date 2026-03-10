# [undocumented-public-class (D101)](#undocumented-public-class-d101)

Added in [v0.0.70](https://github.com/astral-sh/ruff/releases/tag/v0.0.70) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27undocumented-public-class%27%20OR%20D101)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpydocstyle%2Frules%2Fnot_missing.rs#L147)

Derived from the **[pydocstyle](../#pydocstyle-d)** linter.

## [What it does](#what-it-does)

Checks for undocumented public class definitions.

## [Why is this bad?](#why-is-this-bad)

Public classes should be documented via docstrings to outline their purpose
and behavior.

Generally, a class docstring should describe the class's purpose and list
its public attributes and methods.

If the codebase adheres to a standard format for class docstrings, follow
that format for consistency.

## [Example](#example)

```
class Player:
    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points

    def add_points(self, points: int) -> None:
        self.points += points
```

Use instead (in the NumPy docstring format):

```
class Player:
    """A player in the game.

    Attributes
    ----------
    name : str
        The name of the player.
    points : int
        The number of points the player has.

    Methods
    -------
    add_points(points: int) -> None
        Add points to the player's score.
    """

    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points

    def add_points(self, points: int) -> None:
        self.points += points
```

Or (in the Google docstring format):

```
class Player:
    """A player in the game.

    Attributes:
        name: The name of the player.
        points: The number of points the player has.
    """

    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points

    def add_points(self, points: int) -> None:
        self.points += points
```

## [References](#references)

* [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
* [PEP 287 – reStructuredText Docstring Format](https://peps.python.org/pep-0287/)
* [NumPy Style Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
* [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)