# [fast-api-redundant-response-model (FAST001)](#fast-api-redundant-response-model-fast001)

Added in [0.8.0](https://github.com/astral-sh/ruff/releases/tag/0.8.0) ·
[Related issues](https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20(%27fast-api-redundant-response-model%27%20OR%20FAST001)) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fruff_linter%2Fsrc%2Frules%2Ffastapi%2Frules%2Ffastapi_redundant_response_model.rs#L61)

Derived from the **[FastAPI](../#fastapi-fast)** linter.

Fix is always available.

## [What it does](#what-it-does)

Checks for FastAPI routes that use the optional `response_model` parameter
with the same type as the return type.

## [Why is this bad?](#why-is-this-bad)

FastAPI routes automatically infer the response model type from the return
type, so specifying it explicitly is redundant.

The `response_model` parameter is used to override the default response
model type. For example, `response_model` can be used to specify that
a non-serializable response type should instead be serialized via an
alternative type.

For more information, see the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/response-model/).

## [Example](#example)

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item
```

Use instead:

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
```