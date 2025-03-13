
class A:
    def __set_name__(self, owner, name):
        print(self, owner, name)

class B:
    named = A()

def main() -> None:
    print(f'Hello main from : {__file__}')

    b = B()


if __name__ == '__main__':
    main()
