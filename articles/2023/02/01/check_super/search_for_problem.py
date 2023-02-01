


class B:
    def say_hello(self):
        print('Say hello from ', B.__name__, self.__class__.__name__)

class C1(B):
    def say_hello(self):
        print('-- Say hello from ', C1.__name__, self.__class__.__name__)
        return super().say_hello()

class C2(B):
    def say_hello(self):
        print('-- Say hello from ', C2.__name__, self.__class__.__name__)
        return super().say_hello()

    def greetings(self):
        print("Greetings from ", C2.__name__)
        self.say_hello()

class D1(C1, C2):
    def say_hello(self):
        print('-- -- Say hello from ', self.__class__.__name__)
        return super().say_hello()

class D2(C2, C1):
    def say_hello(self):
        print('-- -- Say hello from ', self.__class__.__name__)
        return super().say_hello()

class D3(C1, C2):
    def greetings(self):
        print("Greetings from ", D3.__name__)
        super().greetings()

def main() -> None:
    print(f'Hello main from : {__file__}')

    b = B()
    b.say_hello()
    print("-" * 80)

    d1 = D1()
    d1.say_hello()
    print("-" * 80)

    d2 = D2()
    d2.say_hello()
    print("-" * 80)

    d3 = D3()
    d3.greetings()
    print("-" * 80)

if __name__ == '__main__':
    main()