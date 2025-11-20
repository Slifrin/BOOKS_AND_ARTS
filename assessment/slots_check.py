"""
Docstring for assessment.slots_check
https://docs.python.org/3/reference/datamodel.html#object.__slots__

The action of a __slots__ declaration is not limited to the class where it is defined.
__slots__ declared in parents are available in child classes. However, instances of a child
subclass will get a __dict__ and __weakref__ unless the subclass also defines
__slots__ (which should only contain names of any additional slots).
"""

import sys

class A:
    __slots__ = ['x', 'y']

class B(A):
    __slots__ = ['z']

class C(A): ...


def inspect_obj(obj):
    print('*'*80)
    print(type(obj).__name__)
    if hasattr(obj, '__dict__'):
        for v in vars(obj):
            print(v)
    else:
        for s in obj.__slots__:
            print(s)
    for e in dir(obj):
        print(e)

def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    inspect_obj(A())
    inspect_obj(B())
    inspect_obj(C())


if __name__ == '__main__':
    main()