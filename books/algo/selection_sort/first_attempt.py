"""
    chapter 2
"""



def find_smallest(elements):
    smallest = elements[0]
    smallest_index = 0

    for i in range(1, len(elements)):
        if elements[i] < smallest:
            smallest = elements[i]
            smallest_index = i
    return smallest_index

def sort(elements: list[int]):
    sorted_elements = []
    for i in range(len(elements)):
        smallest = find_smallest(elements)
        sorted_elements.append(elements.pop(smallest))
    return sorted_elements

def use_selectio_sort():
    print("Sorted elements ", sort([5, 3, 6, 2, 10]))


def main() -> None:
    print(f'Hello main from : {__file__}')
    use_selectio_sort()

if __name__ == '__main__':
    main()
