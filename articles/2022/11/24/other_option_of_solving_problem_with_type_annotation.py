"""
    Efective python tip 90
"""

from __future__ import annotations
# 2 correction of problem with type annotations of not yet defined classes 

class ThirdClass:
    def __init__(self, value: FourthClass) -> None:
        self.value  = value


class FourthClass:
    def __init__(self, value: ThirdClass) -> None:
        self.value = value


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()