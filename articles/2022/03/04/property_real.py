"""
https://realpython.com/python-property/

Repeating code of property can be abstracted as descriptor
"""

class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None

class Point:
    y = Coordinate()
    x = Coordinate()

    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    print('Hello main')
    p = Point(12, 5)
    print(p.x)
    print(p.y)

    p.y = 3
    p.y = 'a'

if __name__ == '__main__':
    main()