import functools
import itertools
import numbers

from books.fluent_python.ch_11.tombola import Tombola
from books.fluent_python.ch_11.bingocage import BingoCage

class DumyVector:

    def __init__(self, iterable) -> None:
        self.content = list(iterable)

    def __len__(self):
        return len(self.content)

    def __getitem__(self, position: int): # now it is sequence
        return self.content[position]

    
    def __add__(self, other): # it uses ductyping
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return DumyVector(a + b for a, b in pairs) # new object is created
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return DumyVector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rnum__(self, scalar):
        return self * scalar


class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'rigth operand in += must be {!r} or and iterable'
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self