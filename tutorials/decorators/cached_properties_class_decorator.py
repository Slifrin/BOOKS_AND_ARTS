import time
import random

class cached_property:
    def __init__(self, ttl=300):
        self.ttl = ttl
    
    def __call__(self, fget, doc=None):
        self.fget = fget
        self.__doc__ = doc or fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        return self
    
    def __get__(self, inst, owner):
        now = time.time()
        try:
            value, last_update = inst._cache[self.__name__]
            if self.ttl > 0 and now - last_update > self.ttl:
                raise AttributeError
        except (KeyError, AttributeError):
            value = self.fget(inst)
            try:
                cache = inst._cache
            except AttributeError:
                cache = inst._cache = {}
            cache[self.__name__] =  (value, now)
        return value


class MyClass:
    @cached_property(ttl=600)
    def randint(self):
        return random.randint(0, 100)

def main():
    spr_obj = MyClass()
    print(spr_obj.randint())
    print(spr_obj.randint())

if __name__ == '__main__':
    main()