import logging
import sys


logging.basicConfig(level=logging.INFO)


class LoggedAccess:

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info("Accessing %r giving %r in %r", self.public_name, value, id(self))
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r in %r", self.public_name, value, id(self))
        setattr(obj, self.private_name, value)


class Person:

    name = LoggedAccess()  # First descriptor instance
    age = LoggedAccess()  # Second descriptor instance

    def __init__(self, name, age):
        self.name = name  # Calls the first descriptor
        self.age = age  # Calls the second descriptor

    def birthday(self):
        self.age += 1


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    p = Person("Alice", 30)
    print(getattr(p, "name"))
    print(p.__dict__)
    # print(p.__dict__['age']) # KeyError: 'age'

    print(vars(Person)['name'])

if __name__ == "__main__":
    main()
