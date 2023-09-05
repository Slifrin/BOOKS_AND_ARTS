import asyncio
import sys

import colorama
from colorama import Cursor


colorama.init()


async def print_at(row, text):
    print(Cursor.POS(1, 1 + row) + str(text))
    await asyncio.sleep(0.03)


async def count_lines_in_file(file_num, file_name):
    counter_text = f"{file_name[:20]:<20} "
    with open(file_name, mode="rt", encoding="utf-8") as file:
        for line_num, _ in enumerate(file, start=1):
            counter_text += "□"
            await print_at(file_num, counter_text)
        await print_at(file_num, f"{counter_text} ({line_num})")
        if line_num == 13:
            raise RuntimeError("Files with thirteen lines are too scary!")



async def count_all_files(file_names):
    """
    You can use return_exceptions=True as an argument when awaiting asyncio.gather().
    This will collect exceptions from all your tasks and return them in a list when all
    tasks are finished. However, it’s complicated to then handle these exceptions
    properly, because they’re not using Python’s normal error handling.
    """
    tasks = [
        asyncio.create_task(count_lines_in_file(file_num, file_name))
        for file_num, file_name in enumerate(file_names, start=1)
    ]
    await asyncio.gather(*tasks)

async def count_all_files_but_better(file_names):
    async with asyncio.TaskGroup() as tg:
        for file_num, file_name in enumerate(file_names, start=1):
            tg.create_task(count_lines_in_file(file_num, file_name))

async def main() -> None:
    print(f"Hello main from : {__file__}")
    # await count_all_files(sys.argv[1:])
    await count_all_files_but_better(sys.argv[1:])


if __name__ == "__main__":
    print(colorama.ansi.clear_screen())
    try:
        asyncio.run(main())
    except * UnicodeDecodeError as eg:
        print("Bad encoding:", *[str(e)[:50] for e in eg.exceptions])
    print(Cursor.POS(1, 1 + len(sys.argv)))
