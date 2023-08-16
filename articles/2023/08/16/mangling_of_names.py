
from typing import Any
import inspect
import traceback


def get_mangled_var(obj, var_name):
    for cls in type(obj).__mro__:
        mangled_name = f"_{cls.__name__}{var_name}"
        try:
            val = getattr(obj, mangled_name)
        except AttributeError:
            continue
        return mangled_name, val

    raise AttributeError()


class A:
    def __init__(self):
        self.__x = 123
        self.y = 456


class B(A):
    ...


class C(B):
    def check_mangled_var(self):
        print(get_mangled_var(self, "__x"))

    def __getattr__(self, __name: str) -> Any:
        try:
            var =  super().__getattr__(__name)
        except AttributeError as err:
            caller_frame = inspect.currentframe().f_back
            frame_info = inspect.getframeinfo(caller_frame)
            # print(type(frame_info))
            # print(frame_info.function)
            if frame_info.function == get_mangled_var.__name__:
                raise err
            var = get_mangled_var(self, __name)
            del caller_frame

        return var


def main() -> None:
    print(f'Hello main from : {__file__}')
    c = C()
    print(C.__mro__)
    print(type(c).__mro__)
    c.check_mangled_var()

    print(c.__x)
    print(c.y)


if __name__ == '__main__':
    main()