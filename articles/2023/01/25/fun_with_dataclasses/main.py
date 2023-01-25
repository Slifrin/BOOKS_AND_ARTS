"""
    https://www.youtube.com/watch?v=vRVVyl9uaZc
    many instances and comparing them
    data oriented types
    print
    compare
"""

import dataclasses


@dataclasses.dataclass(order=True)
class Person:
    sort_index: int = dataclasses.field(init=False, repr=False)
    name: str
    job: str
    age: int
    speed: int = 100

    def __post_init__(self):
        self.sort_index = self.speed


@dataclasses.dataclass(order=True, frozen=True)
class ImmutablePerson:
    sort_index: int = dataclasses.field(init=False, repr=False)
    name: str
    job: str
    age: int
    speed: int = 100

    def __post_init__(self):
        """It is frozen so it can not be change in "normal" way"""
        # self.sort_index = self.speed
        # and in not so normal way
        # setattr(self, 'sort_index', self.speed)
        object.__setattr__(self, "sort_index", self.speed)

    def __str__(self) -> str:
        return f"{self.name} {self.job} ({self.age}) with {self.speed}"


def check_people():
    person1 = Person("Bob", "Builder", 40, 200)
    person2 = Person("Tom", "Actor", 33)
    person3 = Person("Tom", "Actor", 33)

    print(person2 == person3)
    print(id(person1), id(person2), id(person3))
    print(person1)

    print(person1 > person3)

    person4 = ImmutablePerson("Bob", "Driver", 300)
    print(person4)
    try:
        person4.speed = 20000
    except dataclasses.FrozenInstanceError:
        print("Can't change frozen object")
    ImmutablePerson.speed = 9999
    for e in dir(ImmutablePerson):
        print(e)
    print("_" * 100)
    for e in ImmutablePerson.__dict__:
        print(e)
    print(ImmutablePerson.__dict__['speed'])

    person5 = ImmutablePerson("John", "Driver", 19)
    print(person5)

    print("_" * 100)
    print("ImmutablePerson.__dict__['__dataclass_params__']")
    print(ImmutablePerson.__dict__['__dataclass_params__'])
    print("_" * 100)
    print("ImmutablePerson.__dict__['__dataclass_fields__']")
    for k, v  in ImmutablePerson.__dict__['__dataclass_fields__'].items():
        print(k, type(v))
    
    ImmutablePerson.__dict__['__dataclass_fields__']["speed"] = 8888
    person6 = ImmutablePerson("Jim", "Driver", 22)
    print(person6)


def main() -> None:

    print(f"Hello main from : {__file__}")
    check_people()


if __name__ == "__main__":
    main()
