# [math-constant (FURB152)](#math-constant-furb152)

Preview (since [v0.1.6](https://github.com/astral-sh/ruff/releases/tag/v0.1.6)) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27math-constant%27%20OR%20FURB152)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Frefurb%2Frules%2Fmath_constant.rs#L30)

Derived from the **[refurb](../#refurb-furb)** linter.

Fix is sometimes available.

This rule is unstable and in [preview](../../preview/). The `--preview` flag is required for use.

## [What it does](#what-it-does)

Checks for literals that are similar to constants in `math` module.

## [Why is this bad?](#why-is-this-bad)

Hard-coding mathematical constants like π increases code duplication,
reduces readability, and may lead to a lack of precision.

## [Example](#example)

```
A = 3.141592 * r**2
```

Use instead:

```
A = math.pi * r**2
```

## [References](#references)

* [Python documentation: `math` constants](https://docs.python.org/3/library/math.html#constants)