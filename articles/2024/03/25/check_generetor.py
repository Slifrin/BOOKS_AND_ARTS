from time import sleep

def my_gen():
    yield 1
    yield 2
    yield 3
    yield 4


def generator_consumer():
    generator = my_gen()
    generator_is_usable = True
    while True:
        new_value = None
        try:
            if generator_is_usable:
                new_value = next(generator)
        except StopIteration:
            print(f'No results to use')
            generator_is_usable = False

        print(f'Got new value {new_value}')
        yield


def main() -> None:
    print(f'Hello main from : {__file__}')
    consumer = generator_consumer()
    while True:
        next(consumer)
        sleep(1)

if __name__ == '__main__':
    main()