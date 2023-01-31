"""
    https://stackoverflow.com/a/1843920
"""

from typing import Any 
from functools import wraps, update_wrapper


class Wrapper:
    def __init__(self, f) -> None:
        self._wrapped_f = f

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("Calling wrapper")
        return self._wrapped_f(*args, **kwargs)


class Wrapper2:
    def __init__(self, x) -> None:
        self.some_var = x
    
    def __call__(self, f) -> Any:
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"Calling wrapper2 with {self.some_var}")
            ret_val = f(*args, **kwargs)
            print("Called wrapper2")
            return ret_val
        return wrapper


class Wrapper3:
    """This looks like does not work due to attributes which function has and class does not

        To access 'wrapped' method use __wrapped__ attr
    """
    def __new__(cls, f):
        print(f'Creating a new {cls.__name__} OBJECT')
        obj = super().__new__(cls)
        print(id(f))
        return update_wrapper(obj, f)


    def __init__(self, f) -> None:
        print(id(f))
        self._wrapped_f = f

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("Calling wrapper3")
        return self._wrapped_f(*args, **kwargs)
    
        
@Wrapper
def hello(x):
    print(f"Say hello to {x}")
        
@Wrapper2(456)
def hello2(x):
    print(f"Say hello to {x}")

 
hello(123)
print(hello)


hello2(234)
print(hello2)


@Wrapper3
def hello3(x):
    print(f"Say hello to {x}")

hello3(345)
print(hello3)