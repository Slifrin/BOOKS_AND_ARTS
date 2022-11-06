"""
    https://www.youtube.com/watch?v=tmeKsb2Fras
"""



from typing import Iterator


def get_values():
    yield "Hello"
    yield "Hello"
    yield 123


def example_get_values():
    gen = get_values()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))

class Range:
    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    def __iter__(self) -> Iterator:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1

def range_example():
    for n in Range(10):
        print(n)

def main() -> None:
    print(f'Hello main from : {__file__}')
    example_get_values()
    range_example()

if __name__ == '__main__':
    main()