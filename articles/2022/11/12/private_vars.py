from pprint import pprint

class Base:
    def __init__(self):
        self._prot = 1
        self.__priv = 2

    def show_priv(self):
        print(f'Priv: {self.__priv}')

    def show_prot(self):
        print(f'Prot: {self._prot}')


class D1(Base):
    def __init__(self):
        print("Derived INIT")
        super().__init__()
    
    def check_piv(self):
        # print(self.__priv) # AttributeError: 'D1' object has no attribute '_D1__priv'
        print(f'{self._Base__priv=}')



def main() -> None:
    print(f'Hello main from : {__file__}')
    b = Base()
    b.show_priv()
    b.show_prot()
    pprint(b.__dict__)

    d = D1()
    d.show_priv()
    d.show_prot()
    pprint(b.__dict__)

    d.check_piv()

if __name__ == '__main__':
    main()