import functools
from typing import Any, Union


@functools.singledispatch
def func(arg: Any, verbose=False):
    raise NotImplementedError(f"Type: {type(arg)} can not be used with {func.__name__}")


@func.register
def _(arg: int | float, verbose=False):
    if verbose:
        print(f"Here's your number {arg}")
        return
    print(f"Number {arg=}")


@func.register
def _(arg: str, verbose=False):
    if verbose:
        print(f"Here's your text {arg}")
        return
    print(f"Text {arg=}")


@func.register(tuple)
def _(arg: str, verbose=False):
    if verbose:
        print(f"Here's your tuple {arg}")
        return
    print(f"tuple {arg=}")


class Negator:

    @functools.singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


"""
# this does not work
class NegatorChild(Negator):
    
    @neg.register
    def _(self, arg: float):
        return -arg
"""


def main() -> None:
    print(f"Hello main from : {__file__}")

    func(1)
    func("Hello")
    func((1, 2, 3))
    try:
        func([1, 2, 3])
    except NotImplementedError as e:
        print(e)

    negator_child = NegatorChild()
    print(negator_child.neg(123))


if __name__ == "__main__":
    main()
