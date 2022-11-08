import module3

def f():
    old_value = module3.MY_CTXVAR.set(2)
    print(f'Module2 current={module3.MY_CTXVAR.get()}, old={old_value}, old type {type(old_value)}')
    module3.MY_CTXVAR.reset(old_value)