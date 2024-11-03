from enum import Enum

from .dummy_class import DummyClass
from .dummy_functions import bye, hello

class Action(Enum):
    BYE = bye
    HELLO = hello

def use_hello():
    print(hello())


class Dummy(Enum):
    FIRST = DummyClass
