from typing import Optional, Union

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_posts = [
    {"id": 1, "title": "First post", "content": "Post 1 content"},
    {"id": 2, "title": "Second post", "content": "Post 2 content"},
    ]


def get_next_id() -> int:
    return max([post["id"] for post in my_posts]) + 1


def find_index(id: int) -> int:
    for idx, p in enumerate(my_posts):
        if p['id'] == id:
            return idx
    raise HTTPException(status_code=404, detail=f"Item with id {id} not found")

def find_post(id: int):
    idx = find_index(id)
    return my_posts[idx]



def remove_post(idx):
    del my_posts[idx]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    raiting: Optional[int] = None


@app.get("/posts")
def read_root():
    return {"data": my_posts}


@app.get("/posts/{item_id}", status_code=status.HTTP_201_CREATED)
def read_item(item_id: int, q: Union[str, None] = None):
    searched_post = find_post(item_id)
    if searched_post is None:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    return {"data": searched_post}


@app.put("/posts/{item_id}")
def update_item(item_id: int, post_content: Post, response: Response):
    print("HELLO")
    print(item_id)
    print(post_content)
    searched_post = find_post(item_id)
    print(response)
    if searched_post is None:
        # response.status_code = status.HTTP_404_NOT_FOUND # raise is better option in this case
        # return {"message": f"Item with id {item_id} not found"}
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    searched_post["title"] = post_content.title
    searched_post["content"] = post_content.content
    searched_post["published"] = post_content.published
    searched_post["raiting"] = post_content.raiting
    return {"data": searched_post}


@app.delete("/posts/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(item_id: int):
    post_idx = find_index(item_id)
    remove_post(post_idx)



@app.post("/posts")
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict["id"] = get_next_id()
    my_posts.append(post_dict)
    return {"new_post": post_dict}