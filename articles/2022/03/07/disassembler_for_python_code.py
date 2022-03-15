"""
    https://docs.python.org/3/library/dis.html
"""

import dis
import pprint

def myfunc(alist):
    return len(alist)

pprint.pprint(dis.dis(myfunc))

byte_code = dis.Bytecode(myfunc)
for inst in byte_code:
    print(inst.opname)