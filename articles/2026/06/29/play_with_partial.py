from functools import partial, partialmethod, Placeholder
import sys


class Cell:
    def __init__(self):
        self._alive = False
    @property
    def alive(self) -> bool:
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)



def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    base_two = partial(int, base=2)

    print(base_two("10010"))
    print(base_two("1001"))

    say_to_world = partial(print, Placeholder, Placeholder, "world")

    say_to_world("one", "two")
    say_to_world("Hello", "there")

    c = Cell()
    print(c.alive)
    c.set_alive()
    print(c.alive)
    c.set_dead()
    print(c.alive)

if __name__ == '__main__':
    main()