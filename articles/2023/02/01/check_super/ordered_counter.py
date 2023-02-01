

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(OrderedDict(self))})"
    def __reduce__(self):
        return self.__class__, (OrderedDict(self), )

def main() -> None:
    print(f'Hello main from : {__file__}')
    oc = OrderedCounter('abracadabra')
    print(oc)
    print(oc.__reduce__())

if __name__ == '__main__':
    main()