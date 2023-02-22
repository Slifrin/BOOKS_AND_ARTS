from typing import Callable

def f1(a, b):
    print("Hello from f1")
    def f2():
        print("Hello from f2")
        print(a, b)
        print(f2.__closure__)
        for cell in f2.__closure__:
            print(cell, cell.cell_contents)
    f2()


def check_closure(f:Callable):
    print("hello form wrapper")

    if not 'functions_to_remember' in globals():
        global functions_to_remember
        functions_to_remember = list()
    functions_to_remember.append(f)

class A:
    __slots__ = ('x',)

    def f(self):
        print(self.f.__func__)
        print(self.f.__self__)

    def to_pass(self):
        check_closure(self.f)


def main() -> None:
    print(f'Hello main from : {__file__}')
    f1(123, 'abc')
    
    # print(help(property))
    A.y = 123
    a = A()
    print(dir(a))

    a.f()
    a.to_pass()


    for f in functions_to_remember:
        f()

if __name__ == '__main__':
    main()