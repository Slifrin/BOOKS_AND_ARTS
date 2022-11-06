"""
    https://www.youtube.com/watch?v=tmeKsb2Fras
"""



import collections
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

def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                value = f(*args)

def sending_to_gen():
    w = worker(str)
    w.send(None) # we need to initialize generator
    w.send([(1,), (2,), (3,)])
    print(next(w)) # return value from yield during next() is none 
    print(next(w))
    print(next(w))

def quiet_worker(f):
    while True:
        w = worker(f)
        try:
            retun_of_subgen = yield from w # passing messages <----> biderational
        except Exception as exc:
            print(f"Ignoring {exc.__class__.__name__}")


def main() -> None:
    print(f'Hello main from : {__file__}')
    # example_get_values()
    # range_example()
    sending_to_gen()


if __name__ == '__main__':
    main()