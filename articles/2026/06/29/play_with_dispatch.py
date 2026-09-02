"""Dispatch happens on the first argument."""

from functools import singledispatch
from typing import Union
from decimal import Decimal
import sys


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: Union[list, set], verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


# For code which doesn’t use type annotations, the appropriate type argument can be passed explicitly to the decorator
@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better then complicate", end=" ")
    print(arg.real, arg.imag)


def nothing(arg, verbose=False):
    print("Nothing")


fun.register(type(None), nothing)

# The register() attribute returns the undecorated function. This enables decorator
# stacking, pickling, and the creation of unit tests for each variant independently:


@fun.register(float)
@fun.register(Decimal)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)


print(f"{fun_num is fun=}")


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    fun("Hello, world.")
    fun("test.", verbose=True)
    fun(42, verbose=True)
    fun([5, 6, 7, 8], verbose=True)
    fun(None)
    fun(1.23)
    print(fun.dispatch(float))
    print(fun.dispatch(Decimal))
    print(fun.dispatch(set))
    print(fun.registry.keys())


if __name__ == "__main__":
    main()
