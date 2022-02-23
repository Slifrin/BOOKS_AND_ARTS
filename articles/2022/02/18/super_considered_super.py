"""
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
"""

import logging
# %%
class LoggingDict(dict):
    def __setitem__(self, __k, v) -> None:
        logging.info()
        return super().__setitem__(__k, v)


# %%
from collections import OrderedDict


class LoggingOD(LoggingDict, OrderedDict):
    pass

from pprint import pprint

pprint(LoggingOD.__mro__)
# %%
print(type(type))
print(type(object))

# %%
class B:
    def __init__(self):
        self.x = 1

    def f(self):
        print("Calling f")
        print(self.__class__.__name__)


class D1(B):
    pass

class B2:
    def __init__(self):
        self.x = 3

class D2(B2, D1):
    def f(self):
        super().f()
        print("After calling super ", self.__class__.__name__)


spr = D2()
print(spr.x)
spr.f()
# %%
class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()
# %%
class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwargs):
        self.moveable = Moveable(x, y)
        super().__init__(**kwargs)

    def draw(self):
        self.moveable.draw()
        super().draw()

class MoveableColoredShape(ColoredShape, MoveableAdapter):
    pass

MoveableColoredShape(color='red', shapename='triangle', x=20, y=20).draw()



# %%
from collections import Counter


class OrderedCounter(Counter, OrderedDict):
    def __repr__(self) -> str:
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
print(oc)
for key, val in oc.items():
    print(key, ' --> ', val)

print(oc.__reduce__())