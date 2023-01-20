"""
    https://python-poetry.org/docs/
"""

import pendulum


def main() -> None:
    print(f'Hello main from : {__file__}')
    now = pendulum.now("Europe/Paris")
    print(now)



if __name__ == '__main__':
    main()