"""
    https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/
    https://www.youtube.com/watch?v=xvb5hGLoK0A&t=1226s


    Use:
        mypy --strict articles/2022/11/05/check_protocols.py
"""

from typing import Protocol


class Flayer(Protocol):
    def fly(self) -> None:
        """A Flyer can fly"""

class FlyingHero:
    """This hero can fly which is BEAST"""
    def fly(self) -> None:
        print("I'm fling")

class RunningHero:
    """This one can run."""
    def run(self) -> None:
        print("I'm running")

class GameBoard:
    """Dummy game board."""
    def mak_fly(self, obj: Flayer) -> None:
        return obj.fly()

def main() -> None:
    print(f'Hello main from : {__file__}')
    board = GameBoard()
    board.mak_fly(FlyingHero())
    board.mak_fly(RunningHero())


if __name__ == '__main__':
    main()