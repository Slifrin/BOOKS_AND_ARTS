import random

def tuple_what():
    # a_tuple = (1, 2)
    # a_tuple[0] += 1 # TypeError: 'tuple' object does not support item assignment

    pros_and_cons = (["Hello", "there"], "Bye")
    pros = pros_and_cons[0]
    pros += ["General"]

    print(pros_and_cons) # (['Hello', 'there', 'General'], 'Bye')
    try:
        pros_and_cons[0] += ["Kenobi"] # TypeError: 'tuple' object does not support item assignment
    except TypeError:
        print("Error buuuut...")

    print(pros_and_cons) # (['Hello', 'there', 'General', 'Kenobi'], 'Bye') xD 


class BadList(list):

    def __add__(self, other):
        print("running custom add")
        return BadList(super(BadList, self).__add__(other))

    def __iadd__(self, other):
        print(f"running custom iadd for {id(self)}")
        return self + other


def plusequals_may_change_pointers():
    x = 1
    print(id(x))
    x += 1
    print(id(x), "changed")

    x = []
    print(id(x))
    x += [1]
    print(id(x), "not changed")

    bad = BadList()
    print(bad, id(bad), "before append")
    bad += [1, 2, 3]  # manual extend
    print(bad, id(bad), "after1 append")
    append_some_to_list(bad)  # might do nothing?
    print(bad, id(bad), "after2 append")


def append_some_to_list(l):
    print(l, id(l))
    l += [4, 5, 6]
    print(l, id(l))


def plusequals_meaning(x, y):
    # x += y
    result = x.__iadd__(y)
    x = result

    # x[0] += y
    result = x[0].__iadd__(y)  # calls __getitem__
    x[0] = result  # calls __setitem__

    # x.val += y
    result = x.val.__iadd__(y)  # calls __getattr__
    x.val = result  # calls __setattr__

class MyId:
    def __init__(self) -> None:
        self.my_id = random.randint(0, 1000)

class OtherList(list):
    ...

def proces2(i):
    print(i, id(i))

def proces1():
    i1 = MyId()
    print(i1.my_id, id(i1))
    proces2(i1)

    l1 = OtherList([1, 2, 3])
    print(l1, id(l1))
    proces2(l1)


def main() -> None:
    print(f'Hello main from : {__file__}')
    # tuple_what()
    plusequals_may_change_pointers()
    # proces1()

if __name__ == '__main__':
    main()