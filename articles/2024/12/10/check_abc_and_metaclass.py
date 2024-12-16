import os
import collections.abc
import sys

from pprint import pprint

import check_tmp

class NewType(type): pass

class GrandParent(): pass

class Parent(GrandParent): pass

class Child(Parent, metaclass=NewType): pass



def main() -> None:
    print(f'Hello main from : {__file__}')
    print(Child.mro())
    print(Child.__class__)
    print(Child.__class__.__name__)
    print(Child.__name__)

    print(os.getcwd())

    pprint(os.environ['PATH'].split(':'))
    pprint(os.environ.items())

    print('*' * 50)

    pprint(sys.path)
    print(check_tmp.hello)


if __name__ == '__main__':
    main()