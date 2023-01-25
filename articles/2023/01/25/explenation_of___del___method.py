"""
    https://www.youtube.com/watch?v=IFjuQmlwXgU
"""
import functools
import tempfile
import shutil
import weakref


def draw_line(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("-"*50, f.__name__, "-" * 50)
        return f(*args, **kwargs)
    return wrapper

class CheckDel:
    def __delitem__(self, key):
        print(f"{self.__class__.__name__}.__delitem__")

    def __delattr__(self, item):
        print(f"{self.__class__.__name__}.__delattr__")

    def __del__(self): # it may never be called due to reference cycles
        print(f"{id(self)=} {self.__class__.__name__}.__del__")



def what_del_is_not():
    x = CheckDel()
    print("\nbefor __delitem__")
    del x[0]
    print("\nbefor __delattr__")
    del x.a
    print("\nbefor __del__")
    del x # it does not call __del__
    print("after __del__\n")

@draw_line
def reference_counting_with_del():
    print("start")
    x = CheckDel()
    y = x # increment reference count
    print(id(x), id(y), f"")
    print("Before del")
    del x # removes name assigned to given object 
    print("end")


@draw_line
def ref_cycle():
    """
        refcounts will not hit zero
        And it is not 100% Guaranteed 
    """
    x = CheckDel()
    y = CheckDel()
    x.children = [y]
    y.parent = x

    # even  when refcount hits 0 it is not guaranteed that __del__ will be called
    # in Cpython it should work hovewer in some cases cleanup can be done during
    # interpreter shutdown
    # exceptions are ignored inside dell

global_x = None
class BadResurectingObject:
    def __del__(self):
        global global_x
        print(f"{id(self)=} {self.__class__.__name__}.__del__")
        global_x = self # refcount is increased and memory will not be freed


class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
    
    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()

    # better it is to use with statment
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.remove()


class BetterTempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        # also exception ignoring behavior
        # but call has stronger guaranteed regarding call
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)
    
    def remove(self):
        self._finalizer() # it is ok to run it multiple times

    @property
    def removed(self):
        return not self._finalizer.alive

    # better it is to use with statment
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.remove()



def main() -> None:
    print(f'Hello main from : {__file__}')
    what_del_is_not()
    reference_counting_with_del()
    ref_cycle()

if __name__ == '__main__':
    main()