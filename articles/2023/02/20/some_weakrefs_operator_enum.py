import weakref
import operator
import enum
import abc
import functools


def check_func():
    def f(x, y, z):
        print(f"{x=}, {y=}, {z=}")

    only_pass_y_z = functools.partial(f, 123)
    only_pass_y_z(42, 21)


def greatings():
    class DummyClass(abc.ABC):

        @abc.abstractmethod
        def greeting(self, x, y):
            ...

    class DummyImplementation(DummyClass):

        def greeting(self, x, y):
            print("Hello there", x, y)
            super().greeting(x, y)

    x = DummyImplementation()
    x.greeting(123, 'abc')


def check_enum():
    ...


def check_operator():
    class DummyClass:
        def __init__(self):
            self.x = 123
            self.y = 456

        def f(self, a, b):
            print(f"Calling from {self}, {a=}, {b=}")

    obj = DummyClass()
    get_x_and_y = operator.attrgetter('x', 'y')
    print(get_x_and_y(obj))

    s = 'abcdef'
    get_items = operator.itemgetter(1, 2)
    print(get_items(s))

    call_methods = operator.methodcaller('f', 123, b='xyz')
    print(call_methods(obj))


def check_ref():
    class DummyClass:
        pass

    x = DummyClass()
    r = weakref.ref(x)
    x2 = r()
    print(x is x2)

    del x, x2
    print(r())

    kenny = DummyClass()
    weakref.finalize(kenny, print, "You killed Kenny!")
    del kenny


def main() -> None:
    print(f'Hello main from : {__file__}')
    check_ref()
    check_operator()
    greatings()
    check_func()

if __name__ == '__main__':
    main()