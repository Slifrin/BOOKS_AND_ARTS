# http://stupidpythonideas.blogspot.com/2015/07/creating-new-sequence-type-is-easy.html

import collections.abc
import math


def simple_exaple():
    def geometric_range(start, stop, factor):
        while start < stop:
            yield start
            start *= factor

    # iterates only once
    for n in geometric_range(10, 10_000, 3):
        print(n)


def virtual_sequence():
    print("*" * 100)

    class GeometricRange(collections.abc.Sequence):
        def __init__(self, start, stop, factor) -> None:
            self.start = start
            self.stop = stop
            self.factor = factor

        def __getitem__(self, index):
            if index < 0 or index >= len(self):
                raise IndexError(f"'{type(self).__name__} object index out of range'")
            return self.start * (self.factor**index)

        def __len__(self):
            return round(math.log(self.stop // self.start, self.factor))

    my_range = GeometricRange(10, 100_000, 3)
    print(f"elemtnt with index 3 {my_range[3]}")

    for n in iter(my_range):
        print(n)

    for i in GeometricRange(10, 100_000, 4):
        print(i)

    my_range2 = GeometricRange(10, 100_000, 5)
    my_r_iter = iter(my_range2)
    print(next(my_r_iter))
    print(next(my_r_iter))
    print(next(my_r_iter))


def virtual_sequence_with_expected_features():
    print("*" * 100)

    # there is a larg number of corner cases :) with generation of ranges
    class GeometricRange(collections.abc.Sequence):
        def __init__(self, start, stop, factor) -> None:
            self.start = start
            self.stop = stop
            self.factor = factor
            self._lenght = round(math.log(self.stop // self.start, self.factor))

        def __getitem__(self, index):
            if isinstance(index, slice):  # support for slices
                start, stop, stride = index.indices(self._lenght)
                start = self[start]
                stop = self[stop] if stop < self._lenght else self.stop
                return type(self)(start, stop, stride)
            if index < 0:
                index += len(self)  # support for negative indices
            if index < 0 or index >= len(self):
                raise IndexError(f"'{type(self).__name__} object index out of range'")
            return self.start * (self.factor**index)

        def __len__(self):
            return round(math.log(self.stop // self.start, self.factor))

        def __repr__(self) -> str:
            return f"{type(self).__name__}({self.start}, {self.stop}, {self.factor})"

        def __eq__(self, other) -> bool:
            return (self.start, self.stop, self.factor) == (
                other.start,
                other.stop,
                other.factor,
            )

        def __hash__(self):
            return hash((type(self), self.start, self.stop, self.factor))

        def __getnewargs__(self):
            """It is method required by pickle"""
            return self.start, self.stop, self.factor

        def _find(self, value):
            return round(math.log(value / self.start, self.factor))

        def index(self, value):
            idx = self._find(value)
            if 0 <= idx < len(self) and self[idx] == value:
                return idx
            raise ValueError(f"{value} is not in range.")

        def __contains__(self, value):
            idx = self._find(value)
            return 0 <= idx < len(self) and self[idx] == value

        def count(self, value):
            return 1 if value in self else 0


def main() -> None:
    print(f"Hello main from : {__file__}")
    simple_exaple()
    virtual_sequence()


if __name__ == "__main__":
    main()
