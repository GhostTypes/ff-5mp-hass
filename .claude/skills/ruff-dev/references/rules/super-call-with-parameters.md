# [super-call-with-parameters (UP008)](#super-call-with-parameters-up008)

Added in [v0.0.155](https://github.com/astral-sh/ruff/releases/tag/v0.0.155) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27super-call-with-parameters%27%20OR%20UP008)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Fpyupgrade%2Frules%2Fsuper_call_with_parameters.rs#L59)

Derived from the **[pyupgrade](../#pyupgrade-up)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Checks for `super` calls that pass redundant arguments.

## [Why is this bad?](#why-is-this-bad)

In Python 3, `super` can be invoked without any arguments when: (1) the
first argument is `__class__`, and (2) the second argument is equivalent to
the first argument of the enclosing method.

When possible, omit the arguments to `super` to make the code more concise
and maintainable.

## [Example](#example)

```
class A:
    def foo(self):
        pass


class B(A):
    def bar(self):
        super(B, self).foo()
```

Use instead:

```
class A:
    def foo(self):
        pass


class B(A):
    def bar(self):
        super().foo()
```

## [Fix safety](#fix-safety)

This rule's fix is marked as unsafe because removing the arguments from a call
may delete comments that are attached to the arguments.

In [preview](https://docs.astral.sh/ruff/preview/), the fix is marked safe if no comments are present.

## [References](#references)

* [Python documentation: `super`](https://docs.python.org/3/library/functions.html#super)
* [super/MRO, Python's most misunderstood feature.](https://www.youtube.com/watch?v=X1PQ7zzltz4)