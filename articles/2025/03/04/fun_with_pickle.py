import dataclasses
import pickle
import sys


@dataclasses.dataclass
class Address:
    city: str
    streat: str


@dataclasses.dataclass
class Person:
    name: str
    age: int
    adressess: list[Address] = dataclasses.field(default_factory=list)


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    file_name = "person.pkl"

    address1 = Address("London", "streat1")
    address2 = Address("Paris", "streat2")

    person = Person("John Doe", 55, [address1, address2])

    with open(file_name, "wb") as file:
        pickle.dump(person, file)

    with open(file_name, "rb") as file:
        new_person = pickle.load(file)
        print(new_person)

    print(person == new_person)


if __name__ == "__main__":
    main()
