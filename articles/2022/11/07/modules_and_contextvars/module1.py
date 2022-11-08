import module3
import module2

def f():
    old_value = module3.MY_CTXVAR.set(1)
    print(f'Module1 current={module3.MY_CTXVAR.get()}, old={old_value}, old type {type(old_value)}')
    module3.MY_CTXVAR.reset(old_value)


def f_with_problems():
    old_value = module3.MY_CTXVAR.set(42)
    try:
        raise KeyError
    except Exception as e:
        print(f'Trobule {e} happend')
    finally:
        module3.MY_CTXVAR.reset(old_value)
    

def main():
    f()
    module2.f()

    module3.MY_CTXVAR.set(13)
    print(f'Before problems {module3.MY_CTXVAR.get()}')
    f_with_problems()
    print(f'After problems {module3.MY_CTXVAR.get()}')



if __name__ == '__main__':
    main()