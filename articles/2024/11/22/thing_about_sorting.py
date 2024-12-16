import operator
import functools
import unicodedata


def first_example():
    x = [5, 2, 3, 1, 4]
    print(x)
    print(x)
    print(sorted(x))
    print(x)
    print(x.sort())
    print(x)

    print(sorted({1: "D", 2: "B", 3: "B", 4: "E", 5: "A"}))

    print(sorted("This is a test string from Andrew".split(), key=str.casefold))

    student_tuples = [
        ("john", "A", 15),
        ("jane", "B", 12),
        ("dave", "B", 10),
    ]
    print(sorted(student_tuples, key=lambda student: student[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


def exaple_with_operator():
    student_tuples = [
        ("john", "A", 15),
        ("jane", "B", 12),
        ("dave", "B", 10),
    ]
    student_objects = [
        Student("john", "A", 15),
        Student("jane", "B", 12),
        Student("dave", "B", 10),
    ]
    print(sorted(student_objects, key=lambda student: student.age))

    print(sorted(student_tuples, key=operator.itemgetter(2)))

    print(sorted(student_objects, key=operator.attrgetter("age")))

    # there are possible multiple levels of sorting
    print(sorted(student_tuples, key=operator.itemgetter(2, 1)))

    print(sorted(student_objects, key=operator.attrgetter("age", "grade")))


def examples_with_data_conversion():
    names = "Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise".split()

    print(sorted(names, key=functools.partial(unicodedata.normalize, "NFD")))

    print(sorted(names, key=functools.partial(unicodedata.normalize, "NFC")))


def example_with_stable_sort():
    student_objects = [
        Student("dave", "B", 10),
        Student("john", "A", 15),
        Student("jane", "B", 12),
    ]

    s = sorted(student_objects, key=operator.attrgetter("age"))
    print(s)
    print(sorted(s, key=operator.attrgetter("grade"), reverse=True))


def decorate_sort_undecorate():
    student_objects = [
        Student("dave", "B", 10),
        Student("john", "A", 15),
        Student("jane", "B", 12),
    ]
    decorated = [
        (student.grade, i, student) for i, student in enumerate(student_objects)
    ]
    decorated.sort()
    undecorateted = [studnet for grade, i, studnet in decorated]
    print(undecorateted)


def example_with_external_source():
    students = ["dave", "john", "jane"]
    newgrades = {"john": "F", "jane": "A", "dave": "C"}
    print(sorted(students, key=newgrades.__getitem__))


def main() -> None:
    """
    Sorts are guaranteed to be stable. That means that when multiple
    records have the same key, their original order is preserved."""
    print(f"Hello main from : {__file__}")
    first_example()
    exaple_with_operator()
    examples_with_data_conversion()
    example_with_stable_sort()
    example_with_external_source()


if __name__ == "__main__":
    main()
