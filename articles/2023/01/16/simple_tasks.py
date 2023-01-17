"""
    Some tasks
"""


def check_sum():
    def get_numbers(n: int):
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                yield i
    numbers = get_numbers(1001)
    print(sum(numbers))

def check_sum2():
    cumulative = 0
    for i in range(1001):
        if i % 3 == 0 or i % 5 == 0:
            cumulative += i
    print(cumulative)

def check_sum3():
    numbers = set(range(3,1000,3)) | set(range(5, 1001, 5))
    print(sum(numbers))
    numbers = set(range(3,1000,3)) & set(range(5, 1001, 5))
    print(sum(numbers))

def check_list():
    l = [1, 5, 9, 2, 4, 3]
    l2 = ["apple", "banana", "orange"]
    l2.sort(key=lambda x: x[-1])
    print(l2)



def main() -> None:
    print(f'Hello main from : {__file__}')

    check_list()
    check_sum()
    check_sum2()
    check_sum3()



if __name__ == '__main__':
    main()