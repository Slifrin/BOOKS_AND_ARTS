# stacks(LIFOs)

from collections import deque
from queue import LifoQueue, Empty


def deque_check():
    s = deque()
    s.append("eat")
    s.append("sleep")
    s.append("code")
    print(s)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    try:
        print(s.pop())
    except IndexError as err:
        print(str(err))


def queue_check():
    s = LifoQueue()
    s.put("1_eat")
    s.put("1_sleep")
    s.put("1_code")
    print(s)

    print(s.get())
    print(s.get())
    print(s.get())
    # next call to get will wait
    try:
        print(s.get_nowait())
    except Empty as err:
        print(str(err))



def main():
    print(f'Hello main from : {__file__}')
    deque_check()
    queue_check()

if __name__ == '__main__':
    main()