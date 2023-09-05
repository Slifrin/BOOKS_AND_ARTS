import sys

def main() -> None:
    print(f'Hello main from : {__file__}')
    try:
        raise ValueError(2342)
    except ValueError:
        print(f"Handling {sys.exception()}")
        print(sys.exc_info()[1] is sys.exception())


    try:
        raise ValueError("098")
    except ValueError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"{exc_type=}  {exc_value=}  {exc_tb=}")
        print(exc_value.__traceback__ is exc_tb)


if __name__ == '__main__':
    main()