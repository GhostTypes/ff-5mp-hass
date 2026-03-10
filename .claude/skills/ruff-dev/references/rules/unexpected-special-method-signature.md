# [unexpected-special-method-signature (PLE0302)](#unexpected-special-method-signature-ple0302)

Added in [v0.0.263](https://github.com/astral-sh/ruff/releases/tag/v0.0.263) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27unexpected-special-method-signature%27%20OR%20PLE0302)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Funexpected_special_method_signature.rs#L112)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for "special" methods that have an unexpected method signature.

## [Why is this bad?](#why-is-this-bad)

"Special" methods, like `__len__`, are expected to adhere to a specific,
standard function signature. Implementing a "special" method using a
non-standard function signature can lead to unexpected and surprising
behavior for users of a given class.

## [Example](#example)

```
class Bookshelf:
    def __init__(self):
        self._books = ["Foo", "Bar", "Baz"]

    def __len__(self, index):  # __len__ does not except an index parameter
        return len(self._books)

    def __getitem__(self, index):
        return self._books[index]
```

Use instead:

```
class Bookshelf:
    def __init__(self):
        self._books = ["Foo", "Bar", "Baz"]

    def __len__(self):
        return len(self._books)

    def __getitem__(self, index):
        return self._books[index]
```

## [References](#references)

* [Python documentation: Data model](https://docs.python.org/3/reference/datamodel.html)