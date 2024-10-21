

def __getattr__(name):
    print(f'There is no {name} in {__name__}')


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()