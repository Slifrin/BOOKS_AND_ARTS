import abc
import sys


class MYabc(abc.ABC):
    pass



def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    MYabc()

if __name__ == '__main__':
    main()