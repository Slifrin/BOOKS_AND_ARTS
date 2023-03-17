import logging
import pathlib
import sys


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

logger = logging.Logger(pathlib.Path(__file__).stem)

# this 
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def main() -> None:
    print(f'Hello main from : {__file__}')
    logger.info("Hello")
    logger.info("Hello there")
    logger.warning("Hello there 222")

if __name__ == '__main__':
    main()