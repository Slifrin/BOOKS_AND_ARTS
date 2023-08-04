from __future__ import annotations # postponed evaluation of annotations

"""
class A:
    def f(self) -> A: # NameError: name 'A' is not defined
        pas


from __future__ import annotations

class A:
    def f(self) -> A:
        pass

"""

from collections.abc import MutableMapping, Mapping, Iterable

def delete_min_key(d: MutableMapping) -> None:
    if not d:
        return
    key = min(d)
    del d[key]


def deep_min(d):
    """dynamic type checking"""
    if isinstance(d, Mapping):
        return min(deep_min(v) for v in d.values())
    elif isinstance(d, Iterable):
        return min(deep_min(v) for v in d)
    else:
        return d
    

def process(config):
    match config:
        case {"route": route}:
            # proccess_route(route)
            pass