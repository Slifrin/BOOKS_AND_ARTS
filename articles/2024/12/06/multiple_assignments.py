
def multiple_assignment_expressions():
    (a := (b := (c := (d := 0))))
    print(a, b, c, d)


def multiple_assignments():
    a = b = c = d = []
    print(a, b, c, d)
    print(a is b)

    tmp = []
    a = tmp
    b = tmp
    c = tmp
    d = tmp


def tricky_assignments():
    a, b = a[:] = [[]], []

    print(a, b)

    #this is same as
    tmp = [[]], []
    a, b = tmp
    a[:] = tmp # this will be recirsive cycle and thats why ther are `...`

    print(a is a[0])

    a, b = a[b] = a = [1, 2, 3], 2
    print(a, b)

def main() -> None:
    print(f"Hello main from : {__file__}")
    multiple_assignment_expressions()
    multiple_assignments()
    tricky_assignments()

    # this is assignment expresiosn
    if x := 1:
        print(x)


if __name__ == "__main__":
    main()
