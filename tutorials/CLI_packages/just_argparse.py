import argparse
import sys


def main() -> None:
    # print(f'Hello main from : {__file__} executed by {sys.executable}')
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()