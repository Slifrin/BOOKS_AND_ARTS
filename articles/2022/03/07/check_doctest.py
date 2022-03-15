"""
    https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python
    https://docs.python.org/3/library/doctest.html
"""


def add(a:int, b:int) -> int:
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()