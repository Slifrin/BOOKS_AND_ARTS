from functools import wraps
from pprint import pprint


def chek_wrapper(method: callable):

    pprint(dir(method))

    pprint(method.__closure__)
    pprint(method.__kwdefaults__)
    pprint(method.__annotations__)
    pprint(method.__class__)
    pprint(method.__defaults__)
    pprint(method.__dict__)

    @wraps(method)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return method(*args, **kwargs)

    return wrapper


class Dummy():
    def __init__(self) -> None:
        self.x = 123
        self.y = 456

    @chek_wrapper
    def some_method(self, a, b='xyz'):
        print(self, self.x, self.y, a, b)



def main() -> None:
    print(f'Hello main from : {__file__}')
    d = Dummy()
    d.some_method(789)

if __name__ == '__main__':
    main()