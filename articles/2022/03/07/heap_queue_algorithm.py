"""
    https://docs.python.org/3/library/heapq.html
    https://realpython.com/python-heapq-module/
"""

"""
Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
This implementation uses arrays for which
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.
"""

import heapq

def main():
    print(f'Hello main from : {__file__}')

    a = [3, 5, 1, 2, 6, 8, 7]
    heapifed_a = heapq.heapify(a)
    print(a)
    print(heapifed_a)

    poped_root = heapq.heappop(a)
    print(a)
    print(poped_root)

    print('*'*40)
    heapq.heappush(a, 4)
    print(a)

    poped_root = heapq.heappop(a)
    print(a)
    print(poped_root)
    poped_root = heapq.heappop(a)
    print(a)
    print(poped_root)
    poped_root = heapq.heappop(a)
    print(a)
    print(poped_root)

if __name__ == '__main__':
    main()