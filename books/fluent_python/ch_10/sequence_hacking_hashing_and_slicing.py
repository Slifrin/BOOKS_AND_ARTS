from array import array
import reprlib
import math
from builtins import ord
import functools
import operator
from typing import Any
import itertools

class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return (len(self) == len(other)) and all(a == b for a, b in zip(self, other))

    def __hash__(self) -> int:
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self._components)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        # return self._components[index]
        # better solution which supports slicis
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, int):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = self.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name: str, value: Any) -> None:
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    
    def angle(self, n):
        r = math.hypot(self)
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
        
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'): # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
            self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
            components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))


def main():
    v1 = Vector([3,4,5])
    print(v1)
    print(abs(v1))

    # after implementation of __len__ & __getitem__

    print(len(v1))
    print(v1[0])
    print(v1[1])
    
    v7 = Vector(range(7))
    print(v7[1:4])
    print(v7[-1])
    try:
        v7[1,2]
    except TypeError as e:
        print(str(e))

    print(v7.y)
    try:
        print(v7.a)
    except AttributeError as e:
        print(str(e))

if __name__ == '__main__':
    main()