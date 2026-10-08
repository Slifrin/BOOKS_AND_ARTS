"""
https://docs.python.org/3/library/contextvars.html

"""

import sys
import asyncio
import contextvars


DEFAULT_VALUE = 42

var: contextvars.ContextVar = contextvars.ContextVar("var", default=DEFAULT_VALUE)


async def some_setting(new_val):
    with var.set(new_val) as previous_token:
        print(type(previous_token))

        assert var.get() == new_val

    assert var.get() == DEFAULT_VALUE

async def show_current_context():
    with var.set(456):
        ctx: contextvars.Context = contextvars.copy_context()
        for k,v in ctx.items():
            print(k, v)
        print("After context print")

async def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    await some_setting(123)
    await show_current_context()

if __name__ == '__main__':
    asyncio.run(main())