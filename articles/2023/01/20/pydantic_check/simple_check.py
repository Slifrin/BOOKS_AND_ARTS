"""
    pydantic helps with validation
"""
import json

import pydantic

from pprint import pprint
from typing import Optional


class ISBNMissingError(Exception):
    """Custom errur due to missing ISBN number."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10Error(Exception):
    """Custom ISBN10 error"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should hev either an ISBN10 or ISBN13",
            )
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value):
        print(f"Running validator for {value}")
        chars = [c for c in value if c in "01234567890Xx"]
        if len(chars) != 10:
            raise ISBN10Error(value=value, message="ISBN10 should be 10 digits")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10Error(value=value, message="ISBN10 should be divisible by 10")
        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True


def check_input():
    with open("input.json") as f:
        data = json.load(f)
        # pprint(data)
        books: list[Book] = [Book(**item) for item in data]
        print(books[0].title)
        # books[0].title = "Hello" # it is immutable
        print(books[0].dict())
        print(books[0].dict(exclude={"price"}))
        print(books[0].dict(include={"price"}))
        print(id(books[0]))
        print(id(books[0].copy()))
        print(id(books[0].copy(deep=True)))

        print(Book.schema_json(indent=4))



def main() -> None:
    print(f"Hello main from : {__file__}")
    check_input()


if __name__ == "__main__":
    main()
