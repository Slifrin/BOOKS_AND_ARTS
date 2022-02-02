import collections
import collections.abc

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    # "required" by protocol of collection

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int) -> Card: # now it is sequence
        return self._cards[position]

    ##############################################################

    # required by collections.abc.MutableSequence ABCs

    def __setitem__(self, position: int, vlaue):
        self._cards[position] = vlaue

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, index: int, value) -> None:
        return self._cards.insert(index, value)


def main():
    deck = FrenchDeck2()


if __name__ == '__main__':
    main()