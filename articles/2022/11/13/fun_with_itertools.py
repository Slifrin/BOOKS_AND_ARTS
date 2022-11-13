"""
    https://www.youtube.com/watch?v=jUM_Dpt6yu0
    https://docs.python.org/3/library/itertools.html
"""

import itertools

def fun_with_permutations():
    items = range(5)
    for index, pem in enumerate(itertools.permutations(items, 3)):
        print(index, pem)

def count_check():
    for i in itertools.count(20):
        print(i)
        if i > 25:
            break


def cycle_check():
    for i, letter in enumerate(itertools.cycle('ABCD')):
        print(letter)
        if i > 9:
            break

def accumulate_check():
    for i in itertools.accumulate([1,2,3,4]):
        print(i)

def combinatoric():
    print("product ", list(itertools.product('ABCD', repeat=2)))
    print("permutations ", list(itertools.permutations('ABCD', 2)))
    print("combinations ", list(itertools.combinations('ABCD', 2)))
    print("combinations_with_replacement ", list(itertools.combinations_with_replacement('ABCD', 2)))

def main() -> None:
    print(f'Hello main from : {__file__}')

    # fun_with_permutations()
    # count_check()
    # cycle_check()
    # accumulate_check()
    combinatoric()

if __name__ == '__main__':
    main()