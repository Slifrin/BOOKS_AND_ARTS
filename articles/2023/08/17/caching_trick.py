import random


def expensive(arg1, arg2, *, _cache={}):
    if (arg1, arg2) in _cache:
        print("Cache HIT!")
        return _cache[(arg1, arg2)]
    print("Performing calcuations")
    result = (lambda x, y: f"{x} and {y}")(arg1, arg2)
    _cache[(arg1, arg2)] = result

    return result


def main() -> None:
    print(f'Hello main from : {__file__}')
    expensive(1, 2)
    expensive(2, 3)
    expensive(1, 2)


if __name__ == '__main__':
    main()