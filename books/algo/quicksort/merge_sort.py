"""
    https://en.wikipedia.org/wiki/Merge_sort
"""

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    left = merge_sort(array[:(len(array) // 2)])
    right = merge_sort(array[(len(array) // 2):])

    return merge(left, right)

def main() -> None:
    print(f'Hello main from : {__file__}')
    array = [3, 5, 2, 1, 4]
    print(merge_sort(array))

if __name__ == '__main__':
    main()
