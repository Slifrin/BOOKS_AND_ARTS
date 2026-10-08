"""
That error means the C version was still used. functools is already imported when Python
starts, because modules like re, typing and collections depend on it. So setting
sys.modules['_functools'] = None came too late, and import functools just
returned the existing C-backed module.

The fix is to reload functools after blocking the C module:
"""


import sys, importlib
sys.modules['_functools'] = None      # block the C accelerator
import functools
importlib.reload(functools)           # re-run functools.py -> pure-Python lru_cache
del sys.modules['_functools']         # optional: undo the block for later imports

@functools.lru_cache(maxsize=None)
def square(x):
    return x * x

square(2); square(5)

# Look up the closure variable named 'cache'
free = dict(zip(square.__code__.co_freevars,
                (c.cell_contents for c in square.__closure__)))
print(free['cache'])   # {2: 4, 5: 25}