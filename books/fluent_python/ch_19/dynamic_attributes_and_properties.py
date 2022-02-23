import warnings

from collections import abc

from dynamic_dict import load


def tmp():
    warnings.warn("Tarapaty")
    print("Witam")

class spr_test:

    def __init__(self, mapping):
        print(mapping)
        self.mapping = mapping

    def my_f(self):
        print('Calling ', self.my_f.__name__)



def main():
    mapping_type = {3 : 'trzy'}
    new_thing = object.__new__(spr_test)
    print(new_thing)
    print(type(new_thing))
    spr_2 = spr_test({1: 'jeden', 2: 'dwa'})
    spr_2.my_f()
    print('!!!!!!', type(spr_2))
    print(spr_2.mapping)

    new_thing.my_f()
    print(new_thing.mapping)

if __name__ == '__main__':
    main()