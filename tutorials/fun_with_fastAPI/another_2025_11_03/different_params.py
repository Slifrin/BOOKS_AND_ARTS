from typing import Annotated, Any, Literal

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()




@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


class FilterParam(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/tools/")
async def read_tools(filter_query: Annotated[FilterParam, Query()]):
    return filter_query