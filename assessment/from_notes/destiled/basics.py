import sys


def set_data_discard():
    s = set()
    try:
        s.remove("Bla")
    except Exception as err:
        print(f"remove:: There was a problem {err}")
    try:
        s.discard("Bla")
    except Exception as err:
        print(f"discard:: There was a problem {err}")


def repr_info():
    class Stack:
        def __init__(self):
            self._items = []

        def push(self, item):
            self._items.append(item)

        def pop(self):
            return self._items.pop()

        def __len__(self):
            return len(self._items)

        def __repr__(self):
            return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>"

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(len(s))
    print(repr(s))
    print(s)


def assignment_of_multiple_values():
    items = [3, 4, 5]
    x, y, z = items
    print(x, y, z)
    a, b, *c = "abcdef"
    print(a, b, c)
    d = {}
    d["x"], d["y"], d["z"] = items
    print(d)
    # number of unpaced locations must mach number of items and iterables on the right.
    datetime = ((5, 19, 2020), (10, 30, "am"))
    (month, day, year), (hour, minute, am_pm) = datetime
    print(f"{month=} {day=} {year=} {hour=} {minute=} {am_pm=}")

    (_, day, _), (hour, _, _) = datetime
    print(f"{day=} {hour=}")

    datetime = ((6, 20, 2021), (11, 31, "pm"))
    (month, *_), (hour, *_) = datetime
    print(f"{month=} {hour=}")

    a = [10, *items, 20]
    b = (*items, 15, 16)
    c = {33, 44, *items}
    print(f"{a=} {b=} {c=}")


def slices_fun():
    a = list(range(10))

    print(a[5:0:-2])
    print(a[:5:-1])
    print(a[5::-1])
    print(a[5:0:-1])

    first_five = slice(0, 5)
    s = 'hello world'
    print(s[first_five])

def operation_on_mutable_sequences():
    a = list(range(6))
    a[1] = 6
    print(a)
    a[2:4] = [10, 11]
    print(a)
    a[3:4] = [-1, -2, -3]
    print(a)
    a[2:] = [0]
    print(a)

    def to_int(x):
        try:
            return int(x)
        except ValueError:
            return None
        
    values = ['1', '2', '-4', 'n/a', '-3', '5']
    print([v for x in values if (v := to_int(x)) is not None])

def evaluateion_order():
    a = 10
    print(a <= 10 and 1 < a)
    # next expression will be evaluated as a <= (10 & 1) < a
    print(a <= 10 & 1 < a)
    print((a <= 10) & (1 < a))

def exceptions_information():
    # e.__cause__ previous exception if exception was intentionally raised in response to handling exception
    # e.__context__ previous exception if previous excetion was raised wile handling other exception
    # e.__traceback__ stack traceback associated with that exception
    pass

def interasting_context_manager():
    class TransactionList:
        def __init__(self, thelist):
            self.thelist = thelist
        def __enter__(self):
            self.workingcopy = list(self.thelist)
            return self.workingcopy
        def __exit__(self, e_type, e_value, e_tb):
            if e_type is None:
                self.thelist[:] = self.workingcopy
            return False # this or None will propagate exception
        
    items = [1,2,3]
    with TransactionList(items) as working_l:
        working_l.append(5)
        working_l.append(6)
    print(items)

    try:
        with TransactionList(items) as working_l:
            working_l.append(8)
            working_l.append(9)
            raise RuntimeError('Tarapaty')
    except RuntimeError:
        pass

    print(items)

def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    set_data_discard()

    repr_info()

    assignment_of_multiple_values()

    slices_fun()

    operation_on_mutable_sequences()

    evaluateion_order()

    interasting_context_manager()

if __name__ == "__main__":
    main()
