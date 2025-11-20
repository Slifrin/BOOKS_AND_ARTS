from typing import Protocol

class Printable(Protocol):
    def __str__(self) -> str:
        pass

def print_obj(obj: Printable) -> None:
    print(str(obj))

class MyClass:
    def __str__(self) -> str:
        return 'This is an instance of MyClass'

class MyOtherClass:
    def __repr__(self) -> str:
        return 'This is an instance of MyOtherClass'

print_obj(MyClass())
print_obj(MyOtherClass())
