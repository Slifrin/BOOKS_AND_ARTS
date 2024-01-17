

class A:
    pass

class B(A):
    pass

class C(B):
    pass



def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()