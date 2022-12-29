"""
    https://rushter.com/blog/python-garbage-collector/
    https://stackify.com/python-garbage-collection/

    https://rushter.com/blog/python-memory-managment/

    There are two aspects to memory management and garbage collection in CPython:

    Reference counting
    Generational garbage collection
"""
import platform
import sys
import gc

def show_implementation():
    print(platform.python_implementation())


def check_ref_count():
    print("Check ref count")
    a = "my-string"
    print(sys.getrefcount(a))
    b = a
    print(sys.getrefcount(a))
    c = [1, 2]
    c.append(a)
    print(sys.getrefcount(a))


class MyClass:
    pass

def reference_cycle():
    print("Check reference cycle")
    a = MyClass()
    print(sys.getrefcount(a))
    a.obj = a
    print(sys.getrefcount(a))
    del a
    

def check_garbage_collector():
    print("Garbage collector info")
    print(gc.get_threshold())
    print(gc.get_count())

    # manual gc
    gc.collect()
    print(gc.get_count())

def main() -> None:
    print(f'Hello main from : {__file__}')
    show_implementation()
    check_ref_count()
    reference_cycle()
    check_garbage_collector()
    print(f"{sys._debugmallocstats()}")

if __name__ == '__main__':
    main()