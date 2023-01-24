"""
    https://docs.python.org/3/library/typing.html#protocols
"""
from abc import ABC, abstractmethod
from typing import Protocol


class NoiseGenerator(Protocol):

    def make_some_noise(self, intensity: int) -> None:
        """"""

class Mosquito:
    def make_some_noise(self):
        """Incorrect implementation
        Runtime Error upon method call!!!
        TypeError: Mosquito.make_some_noise() got an unexpected keyword argument 'intensity'        
        """
        print("Bzzzzzzzz")


def hear_some_noise(generator: NoiseGenerator):
    generator.make_some_noise(intensity=7)


class OtherNoiseGenerator(ABC):

    @abstractmethod
    def make_other_noise(self, vloume: int) -> None:
        """"""

class JetEngine(OtherNoiseGenerator):
    """
        Runtime error upon Object instatiatio!!!
        TypeError: Can't instantiate abstract class JetEngine with abstract method make_other_noise
    """

def main() -> None:
    print(f'Hello main from : {__file__}')
    # hear_some_noise(Mosquito())
    engine = JetEngine()


if __name__ == '__main__':
    main()