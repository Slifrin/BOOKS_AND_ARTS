import random

from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._bals = list(iterable)

    def load(self, iterable):
        self._bals.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._bals))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._bals.pop(position)

    def loaded(self):
        return bool(self._bals)

    def inspect(self):
        return tuple(sorted(self._bals))
    

