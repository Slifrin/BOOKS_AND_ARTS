from functools import cache, lru_cache

# lru least recently used


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=5)
def fib2(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)



def main() -> None:
    print(f'Hello main from : {__file__}')
    for i in range(300):
        print(i, fib(i))
    for i in range(300):
        print(i, fib2(i))
    print("Done")


if __name__ == '__main__':
    main()