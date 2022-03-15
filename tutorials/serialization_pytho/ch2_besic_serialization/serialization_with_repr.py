from collections import namedtuple
from dataclasses import dataclass

class Player:
    """A player in the game"""
    def __init__(self, id, name, keys):
        self.id = id
        self.name = name
        self.keys = keys

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}({self.id!r}, {self.name!r}, {self.keys!r})'


Player2 = namedtuple('Player2', "id, name, keys")

@dataclass
class Player3:
    id: int
    name: str
    keys: str


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO, filename='game.log')

    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    logging.info('p1 is %r', p1)
    
    p2 = Player2(2, 'Parzival', {'copper', 'jade'})
    logging.info('p1 is %r', p2)

    p3 = Player3(3, 'Parzival', {'copper', 'jade'})
    logging.info('p1 is %r', p3)