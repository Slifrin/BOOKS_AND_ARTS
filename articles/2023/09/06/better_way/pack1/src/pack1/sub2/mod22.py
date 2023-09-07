from ..sub1 import mod1

def f() -> None:
    print(f'Hello main from : {__file__}')
    mod1.f()