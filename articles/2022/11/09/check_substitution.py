

class Myclass:
    def f(self):
        print(123)



def main() -> None:
    print(f'Hello main from : {__file__}')
    tmp = Myclass()
    tmp.f()
    print(1)
    def new_f():
        print(456)
    tmp.f = new_f
    print(2)

    tmp.f()

    def new_f2(obj):
        print(789)
    
    Myclass.f = new_f2
    tmp2 = Myclass()
    tmp2.f() 

if __name__ == '__main__':
    main()