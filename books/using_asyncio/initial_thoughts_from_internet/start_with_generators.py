

def check_gen():
    def test():
        val = yield 1
        print(val)
        yield 3
        yield 4

    gen = test()
    print(next(gen))
    print(gen.send(42)) # sending yields
    print(next(gen))


def inner_outer_check():
    def inner():
        inner_result = yield 2
        print("inner ", inner_result)
        return 3

    def outer():
        yield 1
        val = yield from inner()
        print("outer val ", val)
        yield 4

    gen = outer()
    print(next(gen))
    print(next(gen))
    print(gen.send("abc"))


def main() -> None:
    print(f'Hello main from : {__file__}')
    check_gen()
    print("-" * 70)
    inner_outer_check()

if __name__ == '__main__':
    main()