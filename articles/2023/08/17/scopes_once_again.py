x = "global x"

def six():
    def level_six():
        z = "outer z"

        def donkey():
            def inner(y):
                return x, y, z

            z = "donkey z"
            return inner

        def chonky():
            x = "chonky x"
            f = donkey()
            return f("y arg")

        return chonky()
    level_six()

def show_context():

    def level_four_v1():
        z = "first outer z"

        def inner(y):
            return x, y, z

        print(inner.__closure__)
        z = "secound outer z"
        print(inner.__closure__)
        return inner("y arg")
    
    def level_four_v2():
        # z = "first outer z"

        def inner(y):
            return x, y, z

        print(inner.__closure__)
        z = "secound outer z"
        print(inner.__closure__)
        return inner("y arg")

    def level_four_v3():
        # z = "first outer z"

        def inner(y):
            return x, y, z

        print(inner.__globals__)
        z = "secound outer z"
        print(inner.__closure__)
        return inner("y arg")
    
    level_four_v1()
    print("#" * 50)
    level_four_v2()
    print("#" * 50)
    level_four_v3()


def five():
    def level_five(n):
        z = f"oyter z {n}"

        def inner(y):
            return x, y, z
        
        return inner
    
    f = level_five(0)
    g = level_five(1)

    print(f("y arg"), g("other y arg"))


def lambdas_and_comprehensions():
    def lambdas_case():
        return lambda y: (x, y)
    
    f = lambdas_case()
    print(f("arg y"))


def main() -> None:
    print(f"Hello main from : {__file__}")
    print(six())

    print("-" * 50)
    show_context()
    print("-" * 50)
    five()
    print("-" * 50)
    lambdas_and_comprehensions()


if __name__ == "__main__":
    main()
