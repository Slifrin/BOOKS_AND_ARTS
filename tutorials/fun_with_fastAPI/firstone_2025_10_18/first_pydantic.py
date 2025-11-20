import sys

from datetime import datetime
from pprint import pprint

from pydantic import BaseModel, PositiveInt, ValidationError


def basic_example():
    class User(BaseModel):
        id: int
        name: str = "John Doe"
        signup_ts: datetime | None = None
        friends: list[int] = []

    external_data = {
        "id": "123",
        "signup_ts": "2017-06-01 12:22",
        "friends": [1, "2", b"3"],
    }

    user = User(**external_data)
    print(user)
    print(user.id)

def more_things():
    class User(BaseModel):
        id: int
        name: str = "John Doe"
        signup_ts: datetime | None
        tastes: dict[str, PositiveInt]

    external_data = {
        "id": 123,
        "signup_ts": "2019-06-01 12:22",
        "tastes": {
            "wine": 9,
            b"cheese": 7,
            "cabbage": "1",
        },
    }

    user = User(**external_data)
    print(user.id)
    print(user.model_dump())
    print(user.model_dump_json())

    external_data = {"id": "Not an int", "tastes": {}}

    try:
        user_with_error = User(**external_data)
    except ValidationError as err:
        pprint(err.errors())



def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    basic_example()
    more_things()

if __name__ == "__main__":
    main()
