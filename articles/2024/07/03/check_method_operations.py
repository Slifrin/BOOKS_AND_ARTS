
def some_f(**kwargs):
    print(kwargs)


def other_check(**kwargs):
    some_f(**kwargs)


class Tmp:

    def f(self, x):
        print(id(self), x)


def main() -> None:
    print(f"Hello main from : {__file__}")

    func = Tmp.f

    tmp = Tmp()
    print(id(tmp))

    func(tmp, 123)

    other_check(a=12, b=34)




if __name__ == "__main__":
    main()

