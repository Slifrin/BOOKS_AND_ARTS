class A1:
    __slots__ = ('x', 'y')


class B(A1):
    pass

class A2:
    __slots__ = ('z',)


class C(A1, A2):
    pass


def main() -> None:
    print(f'Hello main from : {__file__}')
    tmp1 = A1()
    tmp2 = B()
    try:
        tmp3 = C()
    except TypeError as err:
        print(err)

if __name__ == '__main__':
    main()