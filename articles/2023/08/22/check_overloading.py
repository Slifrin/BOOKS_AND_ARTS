import functools
import typing
import decimal
from pprint import pprint


def check_overload():
    @typing.overload
    def process(message: None) -> None:
        ...

    @typing.overload
    def process(message: int) -> None:
        ...

    def process(message):
        print(f"using {type(message)} -> {message}")

    process(None)
    process(123)
    process("Hello")  # this is static type check error

    pprint(typing.get_overloads(process))


def real_overloading():
    print()
    print(f"{' ' + real_overloading.__name__ + ' ':*^100}")
    print(f"{' ' + real_overloading.__name__ + ' ':*^100}")

    @functools.singledispatch
    def fun(arg, verbose=False):
        if verbose:
            print("Hello there", end=" ")
        print(f"{type(arg)} - {arg}")

    @fun.register
    def _(arg: int | float, verbose=False):
        if verbose:
            print("Strenght in numbers :)", end=" ")
        print(f"{type(arg)} - {arg}")

    @fun.register
    def _(arg: typing.Union[list, set], verbose=False):
        if verbose:
            print("Enumerate this:")

        for i, e in enumerate(arg):
            print(f"{i} - {type(e)} - {e}")

    @fun.register(complex)
    def _(arg, verbose=False):
        if verbose:
            print("Better then complicated.", end=" ")
        print(f"{type(arg)} - {arg.real=} {arg.imag=}")

    def nothing(arg, verbose=False):
        print("Doing nothing")

    fun.register(type(None), nothing)

    @fun.register(float)
    @fun.register(decimal.Decimal)
    def fun_num(arg, verbose=False):
        if verbose:
            print("Half of your number.", end=" ")

        print(arg / 2)

    @fun.register
    def _(arg: dict, verbose=False, very_verbose=False):
        if verbose and very_verbose:
            print("You are about to see a dict.", end=" ")
        print(f"{type(arg)} - {arg}")
        

    fun("Hello World")
    fun("test", verbose=True)
    fun(123, verbose=True)
    fun(["spam", "spam", "eggs", "spam"], verbose=True)
    fun(None)
    fun(21.37, verbose=True)
    fun({"Hello": "There", 42: 2137}, verbose=True, very_verbose=True)

def main() -> None:
    print(f"Hello main from : {__file__}")
    check_overload()
    real_overloading()


if __name__ == "__main__":
    main()
