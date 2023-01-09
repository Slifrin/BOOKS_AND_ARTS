"""
    chapter 4
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # not most optimal choice
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


def main() -> None:
    print(f'Hello main from : {__file__}')
    print(quicksort([10, 5, 2, 3]))

if __name__ == '__main__':
    main()