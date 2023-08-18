from singleton import show_singleton
from builder import show_builder
from observer import show_observer
from iterator import show_iterator
from strategy import show_strategy


def main() -> None:
    print(f'Hello main from : {__file__}')
    show_builder()
    show_singleton()
    show_observer()
    show_iterator()
    show_strategy()

if __name__ == '__main__':
    main()