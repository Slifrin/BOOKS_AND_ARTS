"""
https://effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently
"""

from collections import namedtuple

Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))

ALIVE = '*'
EMPTY = '-'

TICK = object()

def my_corutine():
    while True:
        received = yield
        print("Received : ", received)

def spr():
    it = my_corutine()
    next(it)
    it.send("First")
    it.send("Second")

def count_neighbors(y, x):

    n_ = yield Query(y - 1, x + 0) # North
    ne = yield Query(y - 1, x + 1) # Northeast
    e_ = yield Query(y + 0, x + 1) # East
    se = yield Query(y + 1, x + 1) # Southeast
    s_ = yield Query(y + 1, x + 0) # South
    sw = yield Query(y + 1, x - 1) # Southwest
    w_ = yield Query(y + 0, x - 1) # West
    nw = yield Query(y - 1, x - 1) # Northwest

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY        # Die: Too few
        elif neighbors > 3:
            return EMPTY        # Die: Too meny
    else:
        if neighbors == 3:
            return ALIVE        # Regenerate
    return state

def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)
    
    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def __str__(self) -> str:
        ret_str = ''
        for row in self.rows:
            ret_str += '| '
            for e in row:
                ret_str += e
            ret_str += ' |'
            ret_str += '\n'
        return ret_str

def live_a_generation(grid : Grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:  # Must be a Transition
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


def main():
    print('Hello main')
    
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(2, 2, ALIVE)
    grid.assign(2, 3, ALIVE)
    grid.assign(2, 4, ALIVE)

    print(grid)

    sim = simulate(grid.height, grid.width)

    for _ in range(5):
        grid = live_a_generation(grid, sim)
        print('=' * 20)
        print(grid)


if __name__ == '__main__':
    main()