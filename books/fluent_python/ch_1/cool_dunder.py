import collections
from random import choice
from math import hypot

from __future__ import annotations # doczytac co to jest 

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int) -> Card: # now it is sequence
        return self._cards[position]

def spqdes_high(card: Card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    rank_value = FrenchDeck.ranks.index(card.rank)

    return rank_value * len(suit_values) + suit_values[card.suit]

def cards_game():
    deck = FrenchDeck()
    print(len(deck))

    print(choice(deck), '\n')

    # print("normal iteration")
    # for card in deck:
    #     print(card)
    # print("reversed")
    # for card in reversed(deck):
    #     print(card)

    for card in sorted(deck, key=spqdes_high):
        print(card)

class Vector:
    def __init__(self, x:int = 0, y:int =0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector ({self.x}, {self.y})'
        # return 'Vector (%r, %r)' % (self.x, self.y)
        # return 'Vector (%r, %r)'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, sclalar:int) -> Vector:
        return Vector(self.x * sclalar, self.y * sclalar)



def fun_with_vectors():
    pass

def main():
    fun_with_vectors()

if __name__ == '__main__':
    main()