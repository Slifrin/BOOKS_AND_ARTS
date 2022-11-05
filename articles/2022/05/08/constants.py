
def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const():
    @constant
    def FOO():
        return 123
    @constant
    def BAR():
        return 456

def main():
    print(f'Hello main from : {__file__}')
    CONST = _Const()
    print(CONST.FOO)
    print(CONST.BAR)

    CONST.BAR = 789


if __name__ == '__main__':
    main()