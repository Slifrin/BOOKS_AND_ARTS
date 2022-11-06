"""
    https://www.youtube.com/watch?v=mMbVs17Vmo4
"""

class Property:
    def __init__(self, function_which_implements_get_of_attr):
        self.fget = function_which_implements_get_of_attr

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        print("invoking property :) ")
        return self.fget(obj)


class Student:
    def __init__(self, name) -> None:
        self._name = name

    @Property
    def name(self):
        return self._name

def main() -> None:
    print(f'Hello main from : {__file__}')
    bob = Student('Bob')
    print(bob.name)


if __name__ == '__main__':
    main()