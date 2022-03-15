
"""
    https://docs.python.org/3/library/struct.html
    This module performs conversions between Python values and C structs represented as Python bytes objects. 
"""

import struct

import sys

print(sys.byteorder)

packed_values = struct.pack('hhl', 1, 2, 3)
print(packed_values)
unpacked_values = struct.unpack('hhl', packed_values)
print(unpacked_values)

print("calcsize('hhl')) ", struct.calcsize('hhl'))
print("calcsize('hh')) ", struct.calcsize('hh'))
print("calcsize('l')) ", struct.calcsize('l'))

record = b'raymond   \x32\x12\x08\x01\x08'
print(record)
name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)

from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
new_student = Student._make(struct.unpack('<10sHHb', record))
print(new_student)

print(struct.pack('ci', b'*', 0x12131415))
print(struct.pack('ic', 0x12131415, b'*'))

print("calcsize('ci')", struct.calcsize('ci'))
print("calcsize('ic')", struct.calcsize('ic'))

print("pack('llh0l', 1, 2, 3)", struct.pack('llh0l', 1, 2, 3))

