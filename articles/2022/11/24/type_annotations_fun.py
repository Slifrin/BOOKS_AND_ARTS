"""
    Efective python tip 90
"""


# 1 correction of problem with type annotations of not yet defined classes 
class FirstClass:
    def __init__(self, value: 'SecondClass') -> None:
        self.value  = value


class SecondClass:
    def __init__(self, value: FirstClass) -> None:
        self.value = value

def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()
