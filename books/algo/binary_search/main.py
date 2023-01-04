"""
    Chapter 1
"""

import random

def get_random(n):
    if n < 2:
        raise ValueError
    return list(range(n)), random.randint(0, n-1)

def binary_serach(values, searched_one):
    start = 0
    end = len(values) - 1
    while start <= end:
        half = (start + end) // 2
        guess = values[half]
        if guess == searched_one:
            print("Searched index is ", half)
            return
        elif values[half] > searched_one:
            end = half - 1
        else:
            start = half + 1
    print("NOTHING have been found :(")



def main() -> None:
    print(f'Hello main from : {__file__}')
    values, searched_one = get_random(100)
    print(len(values), searched_one)
    binary_serach(values, searched_one)

if __name__ == '__main__':
    main()
