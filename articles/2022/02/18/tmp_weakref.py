import weakref

class ExpensiveObject:
    def __del__(self):
        print(f'(Deleting {self})')

def on_finalize(*args):
    print(f'on_finalize({args})')

def simple_function(atexit):
    obj = ExpensiveObject()
    f = weakref.finalize(obj, on_finalize, 'arg 1')
    f.atexit = atexit
    print("End of simple_function")

simple_function(False)

obj2 = ExpensiveObject()
f2 = weakref.finalize(obj2, on_finalize, 'arg 2')
f2.atexit = False



# f(True)


# obj2 = ExpensiveObject()
# print(obj2)
# f2 = weakref.finalize(obj2, on_finalize, 'extra argument 2')
# f2.atexit = True