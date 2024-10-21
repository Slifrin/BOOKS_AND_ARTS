"""
https://stackoverflow.com/questions/14413946/what-exactly-is-contained-within-a-obj-closure
"""


def foo():
    def bar():
        print(spam)

    spam = "ham"
    bar()
    spam = "eggs"
    bar()
    return bar

def problems_with_last_capture():

    def foo_2():
        bar = []
        for spam in ("ham", "eggs", "salad"):
            bar.append(lambda: spam)
        return bar

    for bar in foo_2():
        print(bar())

    """prints this:
    salad
    salad
    salad

    as three lambdas reference variable not a value it was bound to
    during object creation.
    """
    



def main() -> None:
    print(f"Hello main from : {__file__}")
    b = foo()
    b()
    print(b.__closure__)
    print(b.__closure__[0].cell_contents)

    problems_with_last_capture()


if __name__ == "__main__":
    main()
