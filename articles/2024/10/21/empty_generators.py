from __future__ import annotations

from collections.abc import Generator


class A:
    def f(self) -> A:
        pass

# Generator[YieldType, SendType, ReturnType]
def first_empty_generator() -> Generator[None, None, None]:
    return
    yield

# Generator[YieldType, SendType, ReturnType]
def better_empty_generator() -> Generator[object, None, None]:
    yield from ()


def main() -> None:
    print(f'Hello main from : {__file__}')

    print(list(first_empty_generator()))
    print(list(better_empty_generator()))


if __name__ == '__main__':
    main()