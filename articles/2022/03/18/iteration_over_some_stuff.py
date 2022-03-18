"""
    https://docs.python.org/3/library/itertools.html
"""

import itertools


def infinite_iteration():
    cyc = itertools.cycle("ABCDE")
    for i in range(10):
        print(next(cyc), end=" ")

    print("\n", "-" * 50, '\n')
    cou = itertools.count(10, 3)
    for i in range(10):
        print(next(cou), end=" ")

    print("\n", "-" * 50, '\n')
    for r in itertools.repeat(9, 4):
        print(r, end=" ")


def iter_termination_on_shortest_item_seq():
    odd_n = [1, 3, 5, 7, 9]
    even_n = [2, 4, 6, 8, 10]
    print("\n", "-" * 50)
    for r in itertools.accumulate(odd_n):
        print(r, end=" ")
    print("\n", "-" * 50)
    for n in itertools.chain(odd_n, even_n):
        print(n, end=" ")

def spr_dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x


def main():
    print(f'Hello main from : {__file__}')
    infinite_iteration()
    iter_termination_on_shortest_item_seq()
    print()
    for x in iter(spr_dropwhile(lambda x: x<5, [1,4,6,4,1])):
        print(x, end=" ")


if __name__ == '__main__':
    main()