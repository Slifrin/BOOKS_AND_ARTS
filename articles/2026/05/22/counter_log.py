import logging


import sys

from collections import Counter

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    c = Counter()
    c["a"] += 1

    logger.info("Info about counter %s", c)

if __name__ == "__main__":
    main()
