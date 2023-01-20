from dataclasses import dataclass
from typing import Callable


@dataclass
class Bard:
    name: str
    instrument: str
    def make_a_noise(self) -> None:
        print(f"My name is {self.name}, Lalalalalalla. Playing {self.instrument}")

def initialize(register_func: Callable) -> None:
    register_func("bard", Bard)
