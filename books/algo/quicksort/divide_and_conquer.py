"""
    chapter 4
"""

from copy import deepcopy


def sum_rerecurent(elements):
    if len(elements) == 0:
        return 0
    else:
        return elements[0] + sum_rerecurent(elements[1:])


def item_count(elements: list):
    try:
        elements.pop()
        return 1 + item_count(elements)
    except IndexError:
        return 0


def maximum(elements: list):
    if len(elements) == 1:
        return elements[0]
    if (other_max := maximum(elements[1:])) > elements[0]:
        return other_max
    return elements[0]


def recursive_binary_search(elements: list, serached_element):
    """"""
    if len(elements) == 0:
        raise IndexError("Element not found")

    mid, rest = divmod(len(elements), 2)
    if elements[mid] == serached_element:
        return mid
    if serached_element > elements[mid]:
        return mid + rest + recursive_binary_search(elements[(mid + 1):],
                                             serached_element)
    else:
        return mid + rest + recursive_binary_search(elements[:mid],
                                             serached_element)


def main() -> None:
    print(f'Hello main from : {__file__}')

    print(sum_rerecurent([1, 2, 3]))
    a = [1, 2, 5, 3, 4]
    print(item_count(deepcopy(a)))
    print(a)
    print(maximum(a))
    b = [1, 2, 3, 4, 5]
    print("SEARCH problems", recursive_binary_search(b, 5))


if __name__ == '__main__':
    main()
