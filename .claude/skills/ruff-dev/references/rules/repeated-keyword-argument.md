# [repeated-keyword-argument (PLE1132)](#repeated-keyword-argument-ple1132)

Added in [0.5.0](https://github.com/astral-sh/ruff/releases/tag/0.5.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27repeated-keyword-argument%27%20OR%20PLE1132)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpylint%2Frules%2Frepeated_keyword_argument.rs#L25)

Derived from the **[Pylint](../#pylint-pl)** linter.

## [What it does](#what-it-does)

Checks for repeated keyword arguments in function calls.

## [Why is this bad?](#why-is-this-bad)

Python does not allow repeated keyword arguments in function calls. If a
function is called with the same keyword argument multiple times, the
interpreter will raise an exception.

## [Example](#example)

```
func(1, 2, c=3, **{"c": 4})
```

## [References](#references)

* [Python documentation: Argument](https://docs.python.org/3/glossary.html#term-argument)