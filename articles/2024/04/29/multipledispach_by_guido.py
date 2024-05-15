"""
https://www.artima.com/weblogs/viewpost.jsp?thread=101605
https://python.plainenglish.io/multiple-dispatch-in-python-72a86da7130c
"""

registry = {}

class MultiMethod:
    def __init__(self, name):
        self.name = name
        self.typename = {}

    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        functio = self.typename.get(types)
        if functio is None:
            raise TypeError("no match")
        return functio(*args)

    def register(self, types, function):
        if types in self.typename:
            raise TypeError("duplicate registration")
        self.typename[types] = function


def multimethod(*types):
    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm
    return register



def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()