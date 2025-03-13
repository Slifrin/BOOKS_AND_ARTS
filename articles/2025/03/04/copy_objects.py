import sys


class Tmp:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'from str {self.__class__} {id(self)} {self.x}'

def printer(collection):
    string = ''
    for item in collection:
        string += f'{item},'

    print(string)


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    l1 = [Tmp(1), Tmp(2), Tmp(3)]
    l2 = l1

    print(f'{id(l1)==id(l2)}, {id(l1), id(l2)}')

    l3 = l1[:]
    print(f'{id(l1)==id(l3)}, {id(l1), id(l3)}')

    printer(l1)
    printer(l2)
    printer(l3)

    l1[1].x = 456
    print('#' * 50)
    printer(l1)
    printer(l2)
    printer(l3)



if __name__ == '__main__':
    main()