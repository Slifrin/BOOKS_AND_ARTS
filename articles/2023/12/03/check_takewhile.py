import itertools


def check_this_while():
    smal_gen = (x for x in range(10))
    def check_predicate(var1):
        print(var1)
        return True


    for elements in itertools.takewhile(check_predicate, smal_gen):
        print(elements)

def more_complex_example():
    """
    output:
        (1, 2)
        (4, 5)
        (7, 8)
    """
    smal_gen = (x for x in range(10))
    processed_elements = None

    def more_complex_predicate(x):
        nonlocal processed_elements
        processed_elements = tuple(itertools.islice(smal_gen, 2))
        return processed_elements

    for _ in itertools.takewhile(more_complex_predicate, smal_gen):
        print(processed_elements)




def main() -> None:
    print(f'Hello main from : {__file__}')
    check_this_while()
    more_complex_example()


if __name__ == '__main__':
    main()