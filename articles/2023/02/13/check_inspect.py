import inspect

from pprint import pprint


class A:
    def f(self):
        frame = inspect.currentframe()
        pprint(frame.f_locals)
        caller_frame = frame.f_back.f_locals
        pprint(caller_frame)


def main() -> None:
    print(f'Hello main from : {__file__}')
    x = 3
    a = A()
    a.f()

if __name__ == '__main__':
    main()