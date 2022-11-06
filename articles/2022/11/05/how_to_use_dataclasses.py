"""
    https://www.infoworld.com/article/3563878/how-to-use-python-dataclasses.html
"""
from dataclasses import dataclass, field, InitVar


@dataclass
class SimpleBook:
    """Object for tracking phisical books."""
    name: str
    weight: float
    shelf_id: int = 0

@dataclass
class MoreComplexBook:
    """Object for tracking phisical books."""
    name: str
    condition: str = field(compare=False)
    weight: float = field(default=0.0, repr=False)
    shelf_id: int = 0
    chapters: list[str] = field(default_factory=list)


    def __post_init__(self):
        if self.condition == "Discarded":
            self.shelf_id = None
        else:
            self.shelf_id = 0

@dataclass
class EvenMoreComplexBook:
    """Object for tracking phisical books."""
    name: str
    condition: InitVar[str] = None
    weight: float = field(default=0.0, repr=False)
    shelf_id: int = 0
    chapters: list[str] = field(default_factory=list)


    def __post_init__(self, condition):
        if condition == "Discarded":
            self.shelf_id = None
        else:
            self.shelf_id = 0

# immutabel dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()