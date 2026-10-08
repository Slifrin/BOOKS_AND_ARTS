"""
Create a memoryview that references object. object must support the buffer protocol.
Built-in objects that support the buffer protocol include bytes and bytearray.
"""

import array
import sys

from functools import wraps

def separator(length: int = 50):
    def inner_separator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('-'* length)
            return f(*args, **kwargs)

        return wrapper
    return inner_separator

@separator(length=80)
def simple_example():
    v = memoryview(b"abcdefg")
    print(v[1])
    print(v[-1])
    print(bytes(v[1:4]))

@separator(length=80)
def indexing_memoryview():
    a = array.array("l", [-11111111, 22222222, -33333333, 44444444])
    m = memoryview(a)
    print(m[0])
    print(m[-1])
    print(m[::2].tolist())

@separator(length=80)
def writing_to_memoryview():
    """
    If the underlying object is writable, the memoryview supports one-dimensional
    slice assignment. Resizing is not allowed
    """
    data = bytearray(b"abcdefg")
    v = memoryview(data)
    print(v.readonly)
    v[0] = ord(b"z")
    print(data)
    v[1:4] = b"123"
    print(data)
    try:
        v[2:3] = b"spam"
    except ValueError as err:
        print(err)
    v[2:6] = b"spam"
    print(data)

@separator()
def hashing_one_dimensional_memoryview():
    v = memoryview(b"abcdefg")
    print(hash(v) == hash(b"abcdefg"))
    print(hash(v[2:4]) == hash(b"cd"))
    print(hash(v[::2]) == hash(b"abcdefg"[::2]))


@separator()
def playing_with_some_funcs():
    a = array.array("l", [1,2,3])
    x = memoryview(a)
    print(f"{x.format=}")
    print(f"{x.itemsize=}")
    print(len(x))
    print(f"{x.nbytes=}")
    y = x.cast("B")
    print(f"{y.format=}")
    print(f"{y.itemsize=}")
    print(len(y))
    print(f"{y.nbytes=}")

    print(f"{x.c_contiguous=}")
    print(f"{x.hex()=}")
    print(f"{x.tobytes()=}")
    print(f"{x.tolist()=}")
    print(f"{x.toreadonly()=}")

    x.release()
    try:
        x[0]
    except ValueError as err:
        print(err)



def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    simple_example()
    indexing_memoryview()
    writing_to_memoryview()
    hashing_one_dimensional_memoryview()
    playing_with_some_funcs()

if __name__ == "__main__":
    main()
