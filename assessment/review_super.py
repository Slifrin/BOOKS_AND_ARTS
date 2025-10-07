"""
Resources:
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/



If our goal is to create a subclass with an MRO to our liking, we need to know how it is calculated.
The basics are simple. The sequence includes the class, its base classes, and the base classes of those
bases and so on until reaching object which is the root class of all classes. The sequence is ordered
so that a class always appears before its parents, and if there are multiple parents, they
keep the same order as the tuple of base classes.



The process of solving those constraints is known as linearization.
There are a number of good papers on the subject, but to create subclasses
with an MRO to our liking, we only need to know the two constraints:
    - children precede their parents
    - the order of appearance in __bases__ is respected.
"""

import logging
import sys

from collections import UserDict, OrderedDict, Counter


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info("Setting %r to %r" % (key, value))
        super().__setitem__(key, value)


class LoggingOrderedDict(LoggingDict, OrderedDict):
    pass


class LoggingDictUser(UserDict):
    def __setitem__(self, key, value):
        logging.info("Setting %r to %r" % (key, value))
        super().__setitem__(key, value)


class LoggingOrderedDictUser(LoggingDictUser, OrderedDict):
    pass


def arguments_stripping():
    # stripping arguments of call
    class Shape:
        def __init__(self, shapename, **kwargs):
            self.shapename = shapename
            super().__init__(**kwargs)

    class ColoredShape(Shape):
        def __init__(self, color, **kwargs):
            self.color = color
            super().__init__(**kwargs)

    cs = ColoredShape(color="red", shapename="circle")


# def defensive_programming():
    # defensive programming of checking if there is no extra method in chain

class Root:
    def draw(self):
        assert not hasattr(super(), "draw")

class Shape(Root):
    def __init__(self, shapename, **kwargs) -> None:
        self.shapename = shapename
        super().__init__(**kwargs)

    def draw(self):
        print(f"Drawing setting shape to: {self.shapename}")
        return super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super().__init__(**kwargs)

    def draw(self):
        print(f"Drawing. Setting color to {self.color} ")
        super().draw()

class IncorrectlyInjected:
    def draw(self):
        print("Tarapaty")
        super().draw()

class CausingTarapaty(Root, IncorrectlyInjected):
    pass

cs = ColoredShape(color="red", shapename="Circle")
cs.draw()

try:
    CausingTarapaty().draw()
except AssertionError as e:
    print("Tarapaty were expected :)")
else:
    print("This was not expected")
    raise RuntimeError("tarapaty x 2")
    

# def incorporation_of_noncooperative_classes():

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwargs):
        self._movable = Moveable(x, y)
        super().__init__(**kwargs)
    def draw(self):
        self._movable.draw()
        super().draw()

    
class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass

def example_of_ordered_counter():
    class OrderedCounter(Counter, OrderedDict):
        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({OrderedDict(self)!r})'
        
        def __reduce__(self): #  related to pickle module https://docs.python.org/3/library/pickle.html#object.__reduce__
            return self.__class__, (OrderedDict(self),)

    oc = OrderedCounter('abracadabra')
    print(repr(oc))

    oc = OrderedCounter('abdccccracadabra')
    print(repr(oc))


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    print(LoggingOrderedDict.__mro__)
    print("*" * 100)
    print(LoggingOrderedDictUser.__mro__)
    # defensive_programming()
    print("*" * 100)
    MovableColoredShape(color='red', shapename='circle', x=10, y=20).draw()

    example_of_ordered_counter()

    position = LoggingOrderedDict.__mro__.index
    print(f'{position(LoggingDict)=} {position(OrderedDict)=}')


if __name__ == "__main__":
    main()
