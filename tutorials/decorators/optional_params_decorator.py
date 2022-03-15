"""
https://realpython.com/primer-on-python-decorators/#more-real-world-examples
"""

import functools
import time


def slow_down(_func=None, *, rate=1):
    """Sleeps given amount of seconds befor calling the function"""

    def decoratr_slow_down(func):
        print("wrap ", func.__name__)
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    # if there is no function it means that decorator is parametriezed due to the fact that
    # calling function is inplicite (syntactic sugra :) and no function is passed 
    # in other case decorator "skips" one step and returns new decorated function
    if _func is None:
        print("Params")
        return decoratr_slow_down
    else:
        print("NO params")
        return decoratr_slow_down(_func)

@slow_down
def f1():
    print("Hello 1")

@slow_down(rate=2)
def f2():
    print("Hello 2")


def main():
    print('Hello main')
    f1()
    f2()

if __name__ == '__main__':
    main()