import traceback
import sys
import logging

from pprint import pformat


def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    try:
        raise Exception("Tarapaty")
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)

        formatted_lines = traceback.format_exc().splitlines()
        print(formatted_lines[0])
        print(formatted_lines[-1])
        print("*** format_exception:")
        print(repr(traceback.format_exception(exc)))
        print("*** extract_tb:")
        print(repr(traceback.extract_tb(exc.__traceback__)))
        logging.exception("Problem detected")

        print("*** before traceback format")
        print(traceback.format_tb(exc.__traceback__))

        print(pformat(repr(traceback.extract_stack())))


if __name__ == '__main__':
    main()