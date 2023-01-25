"""
"""
import pathlib

def main() -> None:
    print(f'Hello main from : {__file__}')
    print(pathlib.Path(__file__).resolve().parent.parent)


if __name__ == '__main__':
    main()