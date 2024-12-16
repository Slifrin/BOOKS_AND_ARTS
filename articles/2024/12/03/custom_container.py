"""
http://stupidpythonideas.blogspot.com/2015/07/creating-new-sequence-type-is-easy.html
"""

import collections.abc
import math


def geometric_ranges_example():
    def geometric_range(start, stop, factor):
        while start < stop:
            yield start
            start *= factor

    class GeometricRange(collections.abc.Sequence):
        def __init__(self, start, stop, factor):
            self.start, self.stop, self.factor = start, stop, factor

        def __getitem__(self, index):
            if index < 0 or index >= len(self):
                raise IndexError(
                    "{} object index out of range".format(type(self).__name__)
                )
            return self.start * (self.factor**index)

        def __len__(self):
            return round(math.log(self.stop // self.start, self.factor))

    tmp = GeometricRange(10, 10000, 3)
    print(tmp[1])


def some_missing_basic_features():

    class GeometricRange(collections.abc.Sequence):
        def __init__(self, start, stop, factor):
            self.start, self.stop, self.factor = start, stop, factor

        def __getitem__(self, index):
            if index < 0 or index >= len(self):
                raise IndexError(
                    "{} object index out of range".format(type(self).__name__)
                )
            return self.start * (self.factor**index)

        def __len__(self):
            return round(math.log(self.stop // self.start, self.factor))

        # those are not provided
        def __repr__(self):
            return "{}({}, {}, {})".format(
                type(self).__name__, self.start, self.stop, self.factor
            )

        # they don't make sens in case of range
        def __eq__(self, other) -> bool:
            return (self.start, self.stop, self.factor) == (
                other.start,
                other.stop,
                other.factor,
            )

        def __hash__(self):
            return hash((type(self), self.start, self.stop, self.factor))


def more_correct_basic_features_and_optimizations():

    class GeometricRange(collections.abc.Sequence):
        def __init__(self, start, stop, factor):
            self.start, self.stop, self.factor = start, stop, factor

        def __getitem__(self, index):
            if index < 0 or index >= len(self):
                raise IndexError(
                    "{} object index out of range".format(type(self).__name__)
                )
            return self.start * (self.factor**index)

        def __len__(self):
            return round(math.log(self.stop // self.start, self.factor))

        # those are not provided
        def __repr__(self):
            return "{}({}, {}, {})".format(
                type(self).__name__, self.start, self.stop, self.factor
            )

        def __eq__(self, other) -> bool:
            if len(self) != len(other):
                return False
            if len(self) == 0:
                return True
            if len(self) == 1:
                return self.start == other.start
            return (self.start, self.factor) == (other.start, other.factor)

        def __hash__(self):
            if len(self) == 0:
                return hash((type(self), 0, None, None))
            if len(self) == 1:
                return hash((type(self), 1, self.start, None))
            return hash((type(self), len(self), self.start, self.factor))

        # it is used by pickle https://docs.python.org/3/library/pickle.html 
        def __getnewargs__(self):
            return self.start, self.stop, self.factor
        
        def _find(self, value):
            return round(math.log(value/self.start, self.factor))

        def index(self, value):
            idx = self._find(value)
            if 0 <= idx < len(self) and self[idx] == value:
                return idx
            
            raise ValueError('{} is not in range'.format(value))

        def __contains__(self, value):
            idx = self._find(value)
            return 0 <= idx < len(self) and self[idx] == value

        def count(self, value):
            return 1 if value in self else 0


def main() -> None:
    print(f"Hello main from : {__file__}")
    geometric_ranges_example()


if __name__ == "__main__":
    main()
