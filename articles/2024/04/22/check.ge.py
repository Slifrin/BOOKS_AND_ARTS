

def simple_thing():
    for x in range(5):
        yield x
    return 9

def simple_thing_v2():
    for x in range(5):
        yield x
    print("Hello there")


def main() -> None:
    print(f'Hello main from : {__file__}')
    for i in simple_thing():
        print(i)
        """
            0
            1
            2
            3
            4
        """
    for i in simple_thing_v2():
        print("-"*10)
        print(i)
        print("*"*10)

if __name__ == '__main__':
    main()
