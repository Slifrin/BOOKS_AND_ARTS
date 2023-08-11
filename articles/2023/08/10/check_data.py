from abc import ABC
from dataclasses import dataclass, astuple


class MyBase(ABC):
    def __init__(self, x):
        self.x = x


@dataclass
class MyDerived(MyBase):
    y: int


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    # def __iter__(self):
    #     yield (self.x, self.y, self.z)
    def __iter__(self):
        yield from astuple(self)


@dataclass
class Vector:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield from astuple(self)

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        return Vector(*(a - b for a, b in zip(self, other)))


def main() -> None:
    print(f"Hello main from : {__file__}")
    tmp = MyDerived(1)
    print([item for item in tmp.__dict__ if not item.startswith("_")])

    new_vector = Vector(1, 2, 3) + Vector(4, 5, 6)
    print(new_vector)

    new_vector = Vector(1, 2, 3) - Vector(4, 5, 6)
    print(new_vector)


if __name__ == "__main__":
    main()
