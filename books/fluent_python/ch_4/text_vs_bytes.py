import struct

fmt = '<3s3sHH'

with open('/Users/Jerzy_Kiedrowski/Desktop/NAUKA/py_fun/books_and_arts/books/fluent_python/ch_4/OpenCommandPalatte.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(header)

print(bytes(header))

print(struct.unpack(fmt, header))


del header
del img

