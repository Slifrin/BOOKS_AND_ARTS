import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.isnstance:
            print("Creation of instance")
            wrapper_singleton.isnstance = cls(*args, **kwargs)
        print("Return instance ", id(wrapper_singleton.isnstance))
        return wrapper_singleton.isnstance
    print("instanciet decorator")
    wrapper_singleton.isnstance = None
    return wrapper_singleton

@singleton
class one:
    pass

@singleton
class two:
    pass

tmp11 = one()
tmp12 = one()
tmp13 = one()

tmp21 = two()
tmp22 = two()
tmp23 = two()