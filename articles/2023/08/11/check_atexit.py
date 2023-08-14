import atexit

def f1():
    print("I'm first")
def f2():
    print("I'm secound")
def f3():
    print("I'm third")




def main() -> None:
    print(f'Hello main from : {__file__}')
    atexit.register(f1)
    atexit.register(f2)
    atexit.register(f3)

if __name__ == '__main__':
    main()