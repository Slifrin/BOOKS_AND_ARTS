import contextlib


class mycontext(contextlib.ContextDecorator):
    def __enter__(self):
        print("starting")
        return self
    
    def __exit__(self, *args):
        print("finishing")
        return False
    

@mycontext()
def function():
    print("The bit in the middle")



def main() -> None:
    print(f'Hello main from : {__file__}')
    function()
    print()
    with mycontext():
        print("Another bit in the middle")

if __name__ == '__main__':
    main()