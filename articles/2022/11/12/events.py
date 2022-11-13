"""
    https://www.youtube.com/watch?v=oNalXg67XEE

    Observer pattern
"""

from collections import defaultdict

actions = defaultdict(list)

def register(event_name, fn):
    actions[event_name].append(fn)

def trigger(event_name, data):
    if not event_name in actions:
        return
    for subscriber in actions[event_name]:
        subscriber(data)


def some_actions():
    def f1(arg):
        print(f'F11 log {arg}')

    def f2(arg):
        print(f'F22 log {arg}')

    register('log', f1)
    register('log', f2)

def run_actions():
    trigger('log', 123)

def main() -> None:
    print(f'Hello main from : {__file__}')
    some_actions()

    run_actions()


if __name__ == '__main__':
    main()
