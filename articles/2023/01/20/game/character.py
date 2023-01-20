from typing import Protocol


class GameCharacter(Protocol):

    def make_a_noise(self) -> None:
        """Make some basic noise"""