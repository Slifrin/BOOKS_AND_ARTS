from collections import abc
from keyword import iskeyword

from dynamic_dict import load

class FrozenJSON:
    """A read-only façade for navigating a JSON-like object
       using attribute notation
    """

    def __new__(cls, arg):  # <1>
        if isinstance(arg, abc.Mapping):
            print("using abc.Mapping")
            return super().__new__(cls)  # <2>
        elif isinstance(arg, abc.MutableSequence):  # <3>
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])  # <4>


def main():
    spr = {
        'a' : [1, 2, 3],
        'b' : {'x' : 'X', 'y' : 'Y'},
    }
    fj = FrozenJSON(spr)
    print(fj)

    print(fj.a)
    print(fj.b)
    print(fj.b.items())

if __name__ == '__main__':
    main()
