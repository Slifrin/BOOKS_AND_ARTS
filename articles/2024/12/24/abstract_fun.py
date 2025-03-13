import abc


class Tmp(abc.ABC):

    @abc.abstractmethod
    def f(self):
        ...



def main() -> None:
    print(f'Hello main from : {__file__}')
    tmp = Tmp()


if __name__ == '__main__':
    main()