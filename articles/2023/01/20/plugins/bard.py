from dataclasses import dataclass

from game import factory

@dataclass
class Bard:
    name: str
    instrument: str
    def make_a_noise(self) -> None:
        print(f"My name is {self.name}, Lalalalalalla. Playing {self.instrument}")

def initialize() -> None:
    factory.register("bard", Bard)
