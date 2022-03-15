"""
def foo():
    bar = []
    for spam in ('ham', 'eggs', 'salad'):
        bar.append(lambda: spam)
    return bar

for bar in foo():
    print bar()
"""

def fun_from_stack():
    def foo():
        bar = []
        for spam in ('ham', 'eggs', 'salad'):
            bar.append(lambda: spam)

        print(bar)
        for b in bar:
            print(b())
        return bar

    for bar in foo():
        print(bar())
        print(bar.__closure__)
        print(type(bar.__closure__))
        for element in bar.__closure__:
            print(element)
            print(type(element))
            print(f"COntent of __closure__ elemnt cell_contents is :: {element.cell_contents}")
            # print(dir(element))

def fun_from_medium():
    """
        https://medium.com/techtofreedom/5-levels-of-understanding-closures-in-python-a0e1212baf6d
    
        1. There are nested functions.
        2. The inner function must use variables defined in its outer function.
        3. The outer function must return the inner function.
    
    """

    def outer_func():
        leader = "???" 

        def print_leader():
            print(leader)

        return print_leader

    f = outer_func()
    del outer_func

    f()


    def solution_to_spam_problem():

        def funcs_generator():
            funcs = []
            for i in range(3):
                def f(j = i):
                    return j * 2
                funcs.append(f)
            return funcs
        
        for f in funcs_generator():
            print(f())

    solution_to_spam_problem()

def main():
    print('Hello main')
    fun_from_medium()

if __name__ == '__main__':
    main()