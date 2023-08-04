

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def __copy__(self):
        return type(self)(self.name)

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.name == other.name
    
    def __repr__(self) -> str:
        # return f"Animal({self.name!r})" # https://stackoverflow.com/questions/44800801/in-python-format-f-string-strings-what-does-r-mean it calls repr of the value supplied
        return f"{type(self).__name__}({self.name})"

class Dog(Animal):
    pass

def normal_usage():
    a = Dog("Dogo")
    print(a)


def main() -> None:
    print(f'Hello main from : {__file__}')
    normal_usage()

if __name__ == '__main__':
    main()