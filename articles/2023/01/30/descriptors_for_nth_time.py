"""

"""
import os
import traceback
import inspect
import pdb

# simple descriptor
class Ten:
    def __get__(self, obj, objtype=None):
        traceback.print_stack()
        for l in inspect.stack():
            print(l)
        pdb.set_trace()
        return 10

class A:
    x = 5
    y = Ten()


class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:
    size = DirectorySize()

    def __init__(self, dirname: str) -> None:
        self.dirname = dirname


def main() -> None:
    print(f'Hello main from : {__file__}')
    dirname = os.path.dirname(__file__)
    print(dirname)
    check_var = A()
    print(A.y)


if __name__ == '__main__':
    main()