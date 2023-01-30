"""
    Instance lookup scans through a chain of namespaces:
        1. Giving data descriptors the highest priority
        2. Followed by instance variables
        3. Then non-data descriptors
        4. Then class variables
        5. Lastly __getattr__() if it is provided.
"""
from typing import Callable

def find_name_in_mro(cls, name, default):
    for base in cls.__mro__:
        if name in vars(base):
            return vars(base)[name]
    return default

def obj_getattribute(obj, name):
    null = object()
    objtype = type(obj)
    cls_var = find_name_in_mro(objtype, name, null)
    descr_get: Callable = getattr(type(cls_var), '__get__', null)
    if descr_get is not null:
        if(hasattr(type(cls_var), '__set__') or hasattr(type(cls_var), '__delete__')):
            return descr_get(cls_var, obj, objtype) # data descriptor
    if hasattr(obj, '__dict__') and name in vars(obj):
        return vars(obj)[name] # instance variables
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype) # non data descriptor
    if cls_var is not null:
        return cls_var # class varaible
    raise AttributeError(name)
