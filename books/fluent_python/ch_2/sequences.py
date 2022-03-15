'''
Container sequences
list, tuple, and collections.deque can hold items of different types.
Flat sequences
str, bytes, bytearray, memoryview, and array.array hold items of one type.

Mutable sequences
list, bytearray, array.array, collections.deque, and memoryview
Immutable sequences
tuple, str, and bytes

'''

import bisect
import array

from collections import deque

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def cool_bisect():

    def demo(bisect_fn):
        print('DEMO:', bisect_fn.__name__)
        print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
        for needle in reversed(NEEDLES):
            position = bisect_fn(HAYSTACK, needle)
            offset = position * '  |'
            print(ROW_FMT.format(needle, position, offset))
    
    demo(bisect.bisect)
    demo(bisect.bisect_left)

def fun_with_memoryview():
    print(fun_with_memoryview.__name__)
    numbers = array.array('h', [-2, -1, 0, 1, 2]) # 'h' means short signed integers
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B') # casting to unsigned char
    print(memv_oct.tolist())
    memv_oct[5] = 4 # this is assigned to most significant byte
    print(memv_oct.tolist())
    print(numbers)

def Deques_and_Other_Queues():
    # The append and popleft operations are atomic, so deque is safe to use as a FIFO
    # queue in multithreaded applications without the need for using locks.
    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)


if __name__ == '__main__':
    cool_bisect()
    print()
    fun_with_memoryview()
    print()
    Deques_and_Other_Queues()

