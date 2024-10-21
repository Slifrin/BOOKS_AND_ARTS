"""
https://stackoverflow.com/questions/847936/how-can-i-find-the-number-of-arguments-of-a-python-function
"""

from inspect import signature, getfullargspec

def simple():
    def example(self, arg1, kwarg1=None):
        pass

    sig = signature(example)

    print(str(sig))
    print(sig.parameters)
    for name, param in sig.parameters.items():
        print(name, param.kind)

    # https://i.sstatic.net/ODvKR.png
    print(example.__code__.co_argcount)
    print(example.__kwdefaults__)
    print(example.__code__.co_kwonlyargcount)
    print(example.__defaults__)

    print(getfullargspec(example))

    

def more_complex():
    def foo(a, b, *, c, d=10):
        pass

    # print all keyword-only arguments without default values:
    sig = signature(foo)
    for param in sig.parameters.values():
        if (param.kind == param.KEYWORD_ONLY and
                        param.default is param.empty):
            print('Parameter:', param)

def counting_args():
    def myfunction(x, s, c=None, d=None):
        pass

    all_args = myfunction.__code__.co_argcount

    if myfunction.__defaults__ is not None:  #  in case there are no kwargs
        kwargs = len(myfunction.__defaults__)
    else:
        kwargs = 0

    print(all_args - kwargs)

    sig = signature(myfunction)
    print(sum(1 for param in sig.parameters.values() if param.kind == param.POSITIONAL_OR_KEYWORD))
    print(sum(1 for param in sig.parameters.values() if param.kind == param.KEYWORD_ONLY))
    print(sum(1 for param in sig.parameters.values() if param.kind == param.POSITIONAL_ONLY))
    print(sum(1 for param in sig.parameters.values() if param.kind == param.VAR_POSITIONAL))
    print(sum(1 for param in sig.parameters.values() if param.kind == param.VAR_KEYWORD))


def main() -> None:
    print(f'Hello main from : {__file__}')
    simple()
    more_complex()
    counting_args()


if __name__ == '__main__':
    main()