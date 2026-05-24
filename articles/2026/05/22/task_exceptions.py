import asyncio
import sys


class Tarapaty(Exception): ...


async def problematic_function():
    raise Tarapaty("There is a problem")



async def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    new_task = asyncio.create_task(problematic_function())

    try:
        await new_task
    except Tarapaty as e:
        print("There was an error of ", str(e))

if __name__ == '__main__':
    asyncio.run(main())