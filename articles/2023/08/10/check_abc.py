import abc


class MYtmp(abc.ABC):
    @abc.abstractmethod
    def __init__(self, x):
        self.x = x

class MyDerived(MYtmp):
    
    def __init__(self, y):
        self.y = y
        super().__init__(y)


def main() -> None:
    print(f'Hello main from : {__file__}')
    try:
        tmp1 = MYtmp(1)
    except TypeError as err:
        print(str(err))
    
    tmp2 = MyDerived(2)
    print(tmp2.__dict__["y"])
    print(tmp2.__dict__["x"])
    print(MyDerived.__mro__)

if __name__ == '__main__':
    main()