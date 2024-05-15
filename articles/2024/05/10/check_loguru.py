"""
https://github.com/Delgan/loguru
"""

import sys

from loguru import logger

logger.add("file_{time}.log")

logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

logger.debug("That's it, beautiful and simple logging!")

new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Here we go!")

@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


def main() -> None:
    print(f'Hello main from : {__file__}')


if __name__ == '__main__':
    main()