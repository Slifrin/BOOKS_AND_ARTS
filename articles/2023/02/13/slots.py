"""
    https://www.youtube.com/watch?v=Iwf17zsDAnY
"""

import sys

def normal_class_example():
    print('Normal class example')

    class A:
        v = 42
        def __init__(self):
            self.x = 'hello'
    
    a = A()
    print(a.x)
    print('a dict: ', a.__dict__)


def slots_class_example():
    print('Slots class example')

    class A:
        __slots__ = ('x',)

        v = 42

        def __init__(self):
            self.x = 'Hello'

    a = A()

    try:
        a.__dict__
    except AttributeError as e:
        print(repr(e))

    try:
        a.y = 'Can not add attributes now'
    except AttributeError as e:
        print(repr(e))

    A.y = 'But can add class varaibles'
    print('a.y not found in a, will be taken from A ----> ', a.y)
    
    print(sys.getsizeof(A()))


def main() -> None:
    print(f'Hello main from : {__file__}')
    normal_class_example()
    slots_class_example()

if __name__ == '__main__':
    main()