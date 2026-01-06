import random

from typing import Annotated


from fastapi import FastAPI, Query
from pydantic import BaseModel, AfterValidator


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()

    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=20,
            pattern="^value$",
        ),
    ] = None,
):
    result = {"item_id": item_id, **item.model_dump()}

    if q:
        result.update({"q": q})


    return result


@app.get("/items/")
async def get_items(
    q: Annotated[
        str | None,
        Query(
            min_length=3,
            max_length=20,
            pattern="^value$",
        ),
    ] = None,
    param1: Annotated[
        str,
        Query(
            min_length=2,
            max_length=20,
        ),
    ] = "some_value",
    multi_value: Annotated[list[str] | None, Query()] = None,
    multi2: Annotated[list, Query()] = [] # using list as default is incorrect
):
    result = {}

    if q:
        result.update({"q": q})

    if param1:
        result.update({"param1": param1})

    if multi_value:
        result.update({"multi_value": multi_value})


    result.update({"multi2_id": id(multi2)})

    return result


@app.get("/pets")
async def read_pets(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}

    return {"hidden_query": "Hidden query not found"}


data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/movies/")
async def read_movies(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "item": item}

