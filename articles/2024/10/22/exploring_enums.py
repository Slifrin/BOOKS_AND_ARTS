from datetime import date
from enum import Enum, Flag, auto, unique
from typing import Any


def simple_usage():
    class Weekday(Enum):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

        @classmethod
        def from_date(cls, date: date):
            return cls(date.isoweekday())

    print(Weekday(3))
    print(Weekday.THURSDAY)
    print(type(Weekday))
    print(type(Weekday.MONDAY))
    print(Weekday.TUESDAY.name, Weekday.TUESDAY.value)

    print(Weekday.from_date(date.today()))


def usage_of_flags():
    class Weekday(Flag):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 4
        THURSDAY = 8
        FRIDAY = 16
        SATURDAY = 32
        SUNDAY = 64

    weekend = Weekday.SATURDAY | Weekday.SUNDAY
    print(weekend, weekend.name, weekend.value)

    for day in weekend:
        print(day)

    chores_for_ethan = {
        "feed the cat": Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
        "do the dishes": Weekday.TUESDAY | Weekday.THURSDAY,
        "answer SO questions": Weekday.SATURDAY,
    }

    def show_chores(chores, day):
        for chore, days in chores.items():
            if day in days:
                print(chore)

    show_chores(chores_for_ethan, Weekday.SATURDAY)


def using_auto_in_enum():
    class Weekday(Flag):
        MONDAY = auto()
        TUESDAY = auto()
        WEDNESDAY = auto()
        THURSDAY = auto()
        FRIDAY = auto()
        SATURDAY = auto()
        SUNDAY = auto()
        WEEKEND = SATURDAY | SUNDAY

    print([member.value for member in Weekday])

    class AutoName(Enum):
        @staticmethod
        def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
            return name

    class Ordinal(AutoName):
        NORTH = auto()
        SOUTH = auto()
        EAST = auto()
        WEST = auto()

    print([member.value for member in Ordinal])

def programmatic_access_to_enumeration_members_and_their_attributes():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3

    print(Color(1))
    print(Color(3))
    print(Color["RED"])
    print(Color["GREEN"])

    class Shape(Enum):
        SQUARE = 2
        DIAMOND = 1
        CIRCLE = 3
        ALIAS_FOR_SQUARE = 2

    print(Shape.SQUARE)
    print(Shape.ALIAS_FOR_SQUARE)
    print(Shape(2))

    print(list(Shape))
    print([(name, member) for name, member in Shape.__members__.items()])
    print([name for name, member in Shape.__members__.items() if name != member.name])


def main() -> None:
    print(f"Hello main from : {__file__}")
    simple_usage()
    usage_of_flags()
    using_auto_in_enum()
    programmatic_access_to_enumeration_members_and_their_attributes()


if __name__ == "__main__":
    main()
