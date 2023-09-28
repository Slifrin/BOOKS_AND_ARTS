


def buble_sort(arr):
    last_element_index = len(arr) - 1
    for last_element in range(last_element_index, 0, -1):
        for i in range(last_element):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def select_sort(arr):
    last_element_index = len(arr) - 1
    for outer in range(last_element_index):
        min_val_idx = outer
        for inner in range(outer + 1, last_element_index + 1):
            if arr[inner] < arr[min_val_idx]:
                min_val_idx = inner
        arr[outer], arr[min_val_idx] = arr[min_val_idx], arr[outer]
    return arr


def insertion_sort(arr):
    for more_then_already_sorted in range(1, len(arr)):
        tmp = arr[more_then_already_sorted]
        idx = more_then_already_sorted
        while idx > 0 and tmp < arr[idx - 1]:
            arr[idx] = arr[idx - 1]
            idx -= 1
        arr[idx] = tmp
    return arr 

def main() -> None:
    print(f'Hello main from : {__file__}')

    print(buble_sort([5, 1, 2, 4, 3, 7, 6]))
    print(select_sort([5, 1, 2, 4, 3, 7, 6]))
    print(insertion_sort([5, 1, 2, 4, 3, 7, 6]))

if __name__ == '__main__':
    main()