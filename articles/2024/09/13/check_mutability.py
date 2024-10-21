
def alter_reality(d):
    d[5] = '5'


def main() -> None:
    print(f'Hello main from : {__file__}')
    d1 = {}
    d2 = {}
    print(f'{d1=} {d2=}')
    alter_reality(d1)
    print(d1)
    alter_reality(d2.copy())
    print(d2)


if __name__ == '__main__':
    main()
