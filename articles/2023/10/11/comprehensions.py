import timeit
import sys

from pprint import pprint


def inspect_comprehensions():
    import dis
    bytecode = compile("[i**2 for i in [1, 2, 3, 4, 5]]", filename="", mode="eval")
    dis.dis(bytecode, depth=0)


def generator_expressions_vs_list_comprehensions():
    print(sys.getsizeof([i for i in range(10000)]))
    print(timeit.timeit("sys.getsizeof(sum([i for i in range(10000)]))", number=10000))

    print( sys.getsizeof((i for i in range(10000))))
    print(timeit.timeit("sys.getsizeof(sum(i for i in range(10000)))", number=10000))


def main() -> None:
    print(f'Hello main from : {__file__}')
    my_list = [ i for i in range(50) if i%2==0 and i%7==0]
    my_list_option2 = [ i for i in range(50) if i%2==0 if i%7==0]
    assert my_list == my_list_option2


    inspect_comprehensions()

    # nested comprehensions
    my_list = [[i*j for j in range(5)] for i in range(5)]
    pprint(my_list)

    # List comprehensions with walrus operator
    with_walrus = [s for num in range(10) if (s := num) % 2 == 0]

    # Using if else
    with_if_else = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(1, 11)]
    print(with_if_else)

    generator_expressions_vs_list_comprehensions()

if __name__ == '__main__':
    main()