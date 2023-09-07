from pack1.sub2.mod2 import f as f1
from pack1.sub2.mod22 import f as f2

def main() -> None:
    print(f'Hello main from : {__file__}')
    print("-"*50)
    f1()
    print("-"*50)
    f2()


if __name__ == '__main__':
    main()