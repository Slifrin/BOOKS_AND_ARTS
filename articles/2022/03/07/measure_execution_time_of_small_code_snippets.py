"""
    https://docs.python.org/3/library/timeit.html
"""

"""
 python3 -m timeit '"-".join(str(n) for n in range(100))'
20000 loops, best of 5: 15.7 usec per loop
❯ python3 -m timeit '"-".join([str(n) for n in range(100)])'
20000 loops, best of 5: 13.5 usec per loop
❯ python3 -m timeit '"-".join(map(str, range(100)))'
20000 loops, best of 5: 11.5 usec per loop


#######################################################################


>>> import timeit
>>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
0.11768093600403517

"""


def main():
    print(f'Hello main from : {__file__}')

def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", number=100000, setup="from __main__ import test"))