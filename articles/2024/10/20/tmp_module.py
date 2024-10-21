import inspect

def foo():
    # for info in inspect.stack()[0]:
    #     print(info)

    print(f"Hello from {inspect.stack()[0][3]}")

def bar():
    print(f"Hello from {inspect.stack()[0][3]}")