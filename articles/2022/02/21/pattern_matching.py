"""
https://www.python-engineer.com/posts/pattern-matching-python/
"""

from dataclasses import dataclass
from enum import Enum

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case _:
            return "Something's wrong with the internet"

@dataclass
class Point:
    x: int
    y: int

def location(point:Point):
    """
    If you are using classes to structure your data, you can use as a pattern
    the class name followed by an argument list that matches the arguments from the constructor.
    This pattern has the ability to capture class attributes into variables.
    """
    match point:
        case Point(x=0, y=0):
            print("Point is original location")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x, y) if x == y:
            print("Fun stuff")

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

def colors_fun(color:Color):
    match color:
        case color.RED:
            print("red")  
        case color.GREEN:
            print("green")
        case color.BLUE:
            print("blue")
            

def main():
    print('Hello main')
    p = Point(0, 13)
    location(p)
    p2 = Point(13, 13)
    location(p2)
    colors_fun(Color(1))

if __name__ == '__main__':
    main()