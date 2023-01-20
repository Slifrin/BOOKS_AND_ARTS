"""
    https://www.youtube.com/watch?v=iCE1bDoit9Q
"""
import json
from dataclasses import dataclass

from game import factory, loader

@dataclass
class Sorcerer:
    name: str
    def make_a_noise(self) -> None:
        print("Aaaaaa")

@dataclass
class Wizard:
    name: str
    def make_a_noise(self) -> None:
        print("Eeeeeee")


@dataclass
class Witcher:
    name: str
    def make_a_noise(self) -> None:
        print("Hmmm")


def hmmm_game():
    factory.register("wizard", Wizard)
    factory.register("sorcerer", Sorcerer)
    factory.register("witcher", Witcher)

    with open("levels.json") as f:
        data = json.load(f)

        plugins = data["plugins"]

        loader.load_plugins(plugins)

        characters = [factory.create(item) for item in data["characters"]]

        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


def main() -> None:
    print(f'Hello main from : {__file__}')
    hmmm_game()

if __name__ == '__main__':
    main()