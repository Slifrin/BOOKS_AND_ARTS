"""
    https://wiki.python.org/moin/Iterator
"""

import random

class RandomIterator:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(['go', 'go', 'stop']) == 'stop':
            raise StopIteration # signals "the end"
        return 1