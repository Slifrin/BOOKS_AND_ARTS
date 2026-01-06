from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


fake_tools_db = [{"tool_name": "Foo"}, {"tool_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, short: bool = False):
    # if q:
    #     return {"item_id": item_id, "q": q}
    # return {"item_id": item_id}
    item: dict[str, int | str | bool] = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


@app.get("/user/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item: dict[str, int | str | bool] = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residulas"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/tools/")
async def read_tool(skip: int = 0, limit: int = 10):
    return fake_tools_db[skip : skip + limit]


@app.get("/cats/{cat_id}")
async def read_cat(cat_id: str, needy: str):
    cat = {"cat_id": cat_id, "needy": needy}
    return cat


@app.get("/dogs/{dog_id}")
async def read_dog_item(
    dog_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    # In this case, there are 3 query parameters:
    # needy, a required str.
    # skip, an int with a default value of 0.
    # limit, an optional int.
    dog = {"dog_id": dog_id, "needy": needy, "skip": skip, "limit": limit}
    return dog