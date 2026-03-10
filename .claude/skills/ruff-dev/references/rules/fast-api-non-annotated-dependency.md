# [fast-api-non-annotated-dependency (FAST002)](#fast-api-non-annotated-dependency-fast002)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27fast-api-non-annotated-dependency%27%20OR%20FAST002)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ffastapi%2Frules%2Ffastapi_non_annotated_dependency.rs#L81)

Derived from the **[FastAPI](../#fastapi-fast)** linter.

Fix is sometimes available.

## [What it does](#what-it-does)

Identifies FastAPI routes with deprecated uses of `Depends` or similar.

## [Why is this bad?](#why-is-this-bad)

The [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/?h=annotated#advantages-of-annotated) recommends the use of [`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated)
for defining route dependencies and parameters, rather than using `Depends`,
`Query` or similar as a default value for a parameter. Using this approach
everywhere helps ensure consistency and clarity in defining dependencies
and parameters.

`Annotated` was added to the `typing` module in Python 3.9; however,
the third-party [`typing_extensions`](https://typing-extensions.readthedocs.io/en/stable/) package
provides a backport that can be used on older versions of Python.

## [Example](#example)

```
from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

Use instead:

```
from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
```

## [Fix safety](#fix-safety)

This fix is always unsafe, as adding/removing/changing a function parameter's
default value can change runtime behavior. Additionally, comments inside the
deprecated uses might be removed.

## [Availability](#availability)

Because this rule relies on the third-party `typing_extensions` module for Python versions
before 3.9, if the target version is < 3.9 and `typing_extensions` imports have been
disabled by the [`lint.typing-extensions`](../../settings/#lint_typing-extensions) linter option the diagnostic will not be emitted
and no fix will be offered.

## [Options](#options)

* [`lint.typing-extensions`](../../settings/#lint_typing-extensions)