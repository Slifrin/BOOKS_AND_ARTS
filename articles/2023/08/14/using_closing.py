import contextlib
from urllib.request import urlopen


def check_closing():
    with contextlib.closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


# from contextlib import asynccontextmanager
# @asynccontextmanager
# async def aclosing(thing):
#     try:
#         yield thing
#     finally:
#         await thing.aclose()

async def a_check_closing():
    async with contextlib.aclosing(my_generator()) as values:
        async for value in values:
            if value == 42:
                break




def main() -> None:
    print(f'Hello main from : {__file__}')

    check_closing()

if __name__ == '__main__':
    main()