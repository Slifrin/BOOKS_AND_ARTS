import pendulum
import sys


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    today = pendulum.today()
    yesterday = pendulum.yesterday()
    some_old_date = yesterday.subtract(years=3)

    print(today)
    print(yesterday)
    print(some_old_date)

    print(dir(today - yesterday))
    print((today - yesterday).in_years())
    print(int((today - yesterday).in_years()))

    print((today - some_old_date).in_years())
    print(int((today - some_old_date).in_years()))


if __name__ == '__main__':
    main()