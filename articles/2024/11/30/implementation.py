"""
mypy
error: Only concrete class can be given where "Type[Base]" is expected
Found 1 error in 1 file (checked 1 source file)
"""

import abc
import collections.abc
from dataclasses import dataclass
from typing import List


@dataclass
class Base(abc.ABC):
    a: str

    def __post_init__(self):
        self.a = self.a.upper()

    @abc.abstractmethod
    def process(self) -> str:
        pass


@dataclass
class Implementation(Base):
    b: str

    def __post_init__(self):
        super().__post_init__()
        self.b = self.b.lower()

    def process(self) -> str:
        return f"{self.a} {self.b}"


@dataclass
class DerivedList(List):
    c: List[str]

    def __contains__(self, item: object) -> bool:
        return item in self.c

    def capitalize(self) -> List[str]:
        return [e.upper() for e in self.c]
