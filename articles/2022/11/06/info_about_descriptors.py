"""
    https://www.youtube.com/watch?v=mMbVs17Vmo4
"""

class Descriptor:
    """ Object is descriptor if it implements any of this methods
        Those methods are difined per atribute they 

        And __getattr__, __setattr__ and __delatr__ are difiened per class!!!!
        For them class decides how to access atribiutes 

        For Descriptors ATRIBUTE ITSELF decides how it is accessed

    """

    def __get__(self, obj, owner=None): # owner aka objtype is to do different things for instance and class itself
        print(f"call to get on {obj=} {owner=}")

    def __set__(self, obj, value):
        print("call to set")

    def __delete__(self, obj):
        print("call to del")

class SomeClass:
    x = Descriptor()

def check_descriptors():
    obj = SomeClass()

    print(obj.x)
    print(SomeClass.x)

    obj.x = 42
    del obj.x

def inspect_prperty():
    class Rect:
        def __init__(self, w, h):
            self.width = w
            self.hight = h
        


def descriptors_hiden_in_plain_sight():
    # 1 functions :)
    class A:
        def f():
            return None
    print(A.f)
    print(A().f)

    # 2 @property

    # 3 classmethod, staticmethod

    # 4 Slots whatch about this 

    # 5 __dict__ :)

    # 6 SQLAlchemy

    # 7 Field Validation

    # 8 super lookaps


def main() -> None:
    print(f'Hello main from : {__file__}')
    check_descriptors()
    descriptors_hiden_in_plain_sight()

if __name__ == '__main__':
    main()