from functools import wraps
from inspect import isgeneratorfunction




def decorator_with_check(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        print("hello from function_wrapper decorator_with_check")
        return func(*args, **kwargs)

    @wraps(func)
    def generator_wrapper(*args, **kwargs):
        print("hello from generator_wrapper decorator_with_check")
        yield from func(*args, **kwargs)

    if isgeneratorfunction(func):
        return generator_wrapper

    return function_wrapper

def decorator_with_check_no_wraps(func):
    def function_wrapper(*args, **kwargs):
        print("hello from function_wrapper decorator_with_check_no_wraps")
        return func(*args, **kwargs)

    def generator_wrapper(*args, **kwargs):
        print("hello from generator_wrapper decorator_with_check_no_wraps")
        yield from func(*args, **kwargs)

    if isgeneratorfunction(func):
        return generator_wrapper

    return function_wrapper


def decorator_with_no_check(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        print("hello from function_wrapper decorator_with_no_check")
        return func(*args, **kwargs)

    return function_wrapper

def decorator_with_no_check_no_wraps(func):
    def function_wrapper(*args, **kwargs):
        print("hello from function_wrapper decorator_with_no_check_no_wraps")
        return func(*args, **kwargs)

    return function_wrapper


# @decorator_with_check
# def simple_gen_1():
#     print("Init simple_gen_1")
#     for i in range(2):
#         yield i

# @decorator_with_no_check
# def simple_gen_2():
#     print("Init simple_gen_2")
#     for i in range(2):
#         yield i

@decorator_with_check_no_wraps
def simple_gen_3():
    print("Init simple_gen_1")
    for i in range(2):
        yield i

@decorator_with_no_check_no_wraps
def simple_gen_4():
    print("Init simple_gen_2")
    for i in range(2):
        yield i


def main() -> None:
    print(f'Hello main from : {__file__}')

    # instance_1 = simple_gen_1()
    # print(id(instance_1), type(instance_1), instance_1)

    # instance_2 = simple_gen_2()
    # print(id(instance_2), type(instance_2), instance_2)

    instance_3 = simple_gen_3()
    print(id(instance_3), type(instance_3), instance_3)

    instance_4 = simple_gen_4()
    print(id(instance_4), type(instance_4), instance_4)


if __name__ == '__main__':
    main()