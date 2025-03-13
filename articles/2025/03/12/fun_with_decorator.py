from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return func(*args, **kwargs)

    wrapper.counter = 0
    return wrapper


@count_calls
def hello_world():
    print('Hello world')


hello_world()
print(hello_world.counter)
print(dir(hello_world))


def count_calls2(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        func.counter += 1
        return func(*args, **kwargs)
    # it is kind of stupide ;) check if that can work
    def custom_attr_getter(self, name):
        obj = getattr(self.__wrapped__, name)
        return obj

    wrapper.__getattr__ = custom_attr_getter
    func.counter = 0

    return wrapper


@count_calls2
def hello_world2():
    print('Hello world')


hello_world2()
# print(hello_world2.__wrapped__.counter)
print(hello_world2.counter)
