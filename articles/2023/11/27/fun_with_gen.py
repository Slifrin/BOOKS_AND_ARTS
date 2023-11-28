from itertools import islice, zip_longest


def fun_with_islice():
    def example_one():
        print(f"Running {example_one.__name__}")
        not_so_well_reversed = reversed(list(range(5)))
        some_values = tuple(islice(not_so_well_reversed, 2))
        while some_values:
            print(some_values)
            some_values = tuple(islice(not_so_well_reversed, 2))
        print(f"End of {example_one.__name__}")

    def example_two():
        print(f"Running {example_two.__name__}")
        not_so_well_reversed = reversed(list(range(5)))
        while some_values := tuple(islice(not_so_well_reversed, 2)):
            print(some_values)
        print(f"End of {example_two.__name__}")

    def example_three():
        print(f"Running {example_three.__name__}")
        not_so_well_reversed = reversed(list(range(5)))
        while True:
            some_values = tuple(islice(not_so_well_reversed, 2)) # will return empty container
            print(some_values)
        print(f"End of {example_three.__name__}")

    example_one()
    example_two()
    # example_three()


def fun_with_zip_longest():
    def my_gen():
        for x in range(10):
            yield x

    for x in zip_longest(*[iter(my_gen())] * 3, fillvalue="FILLVALUE"):
        print(x)


def fun_with_gen():
    def my_gen():
        for x in range(5):
            yield
        print("After yielding all values")
        return

    gen = my_gen()
    for val in gen:
        print(val)

    gen2 = my_gen()
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    print(next(gen2))
    try:
        print(next(gen2))
    except StopIteration as e:
        print(f"There was expected {e}")


def main() -> None:
    print(f"Hello main from : {__file__}")
    fun_with_gen()
    fun_with_islice()
    fun_with_zip_longest()


if __name__ == "__main__":
    main()
