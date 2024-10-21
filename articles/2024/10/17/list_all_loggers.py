"""
https://stackoverflow.com/questions/53249304/how-to-list-all-existing-loggers-using-python-logging-module
"""

import logging
from pprint import pprint


def list_all_loggers():
    logging.root.manager.loggerDict
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    pprint(loggers)


def main() -> None:
    print(f"Hello main from : {__file__}")
    list_all_loggers()


if __name__ == "__main__":
    main()
12