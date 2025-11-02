import sys
from typing import Union, Optional, Annotated

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_full_name_with_types(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def process_items(items: list[str]) -> None:
    for item in items:
        print(item)


def process_items_2(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_dict_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)


def union_types_old(item: Union[int, str]):
    print(item)


def union_types_new(item: int | str):
    print(item)


def func_with_optional_param(name: Optional[str] = None):
    if name is not None:
        print(f"Hello {name}!")
    else:
        print("Hello World")


def also_valid_optional(name: str | None = None):
    if name is not None:
        print(f"Hello {name}!")
    else:
        print("Hello World")

def also_valid_optional_2(name: Union[str, None] = None):
    if name is not None:
        print(f"Hello {name}!")
    else:
        print("Hello World")


def extra_metadata(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    print(get_full_name("john", "doe"))


if __name__ == '__main__':
    main()

