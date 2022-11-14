"""
    https://valarmorghulis.io/tech/201904-contextvars-and-thread-local/
"""

import contextvars
import asyncio
import functools
import random
import threading
import time

context_var = contextvars.ContextVar("test", default=['root'])


class ValueLocal(threading.local):
    def __init__(self, value):
        self.value = value

thread_local = ValueLocal(['root'])


INITIAL_STATE = {
    "contextvars": "",
    "thread.local": ""
}

outputs = {
    "contextvars": "",
    "thread.local": ""
}

def dump_context(x):
    '''
    Dump the contextvars and thread.local to outputs.
    '''
    outputs["contextvars"] += "%s\t%s\n" % (x, '\t'.join(context_var.get()))
    outputs["thread.local"] += "%s\t%s\n" % (x, '\t'.join(thread_local.value))

def async_function_context(f):
    '''
    A wrapper for async/await functions.
    '''
    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        context_var.set(context_var.get()[:] + [f.__name__])
        thread_local.value = thread_local.value[:] + [f.__name__]
        r = await f(*args, **kwargs)
        context_var.set(context_var.get()[:-1])
        thread_local.value = thread_local.value[:-1]
        return r
    return wrapper

def function_context(f):
    """
    A wrapper of normal functions.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        context_var.set(context_var.get()[:] + [f.__name__])
        thread_local.value = thread_local.value[:] + [f.__name__]
        r = f(*args, **kwargs)
        context_var.set(context_var.get()[:-1])
        thread_local.value = thread_local.value[:-1]
        return r
    return wrapper

def threading_example():

    @function_context
    def foo(x):
        time.sleep(random.random())
        dump_context(x)
        bar(x)
        dump_context(x)

    @function_context
    def bar(x):
        time.sleep(random.random())
        dump_context(x)
        baz(x)
        dump_context(x)

    @function_context
    def baz(x):
        time.sleep(random.random())
        dump_context(x)

    threads = [threading.Thread(target=foo, args=(i,)) for i in [1, 2, 3]]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for key, value in outputs.items():
        print("***%s***\n%s" % (key, value))

async def asyncio_example():
    async def foo(x):
        await asyncio.sleep(random.random())
        dump_context(x)
        await bar(x)
        dump_context(x)
    
    async def bar(x):
        await asyncio.sleep(random.random())
        dump_context(x)
        await baz(x)
        dump_context(x)

    async def baz(x):
        await asyncio.sleep(random.random())
        dump_context(x)

    await asyncio.gather(
        foo(1),
        foo(2),
        foo(3)
    )
    for key, value in outputs.items():
        print("***%s***\n%s" % (key, value))


def main1() -> None:
    print(f'Hello main from : {__file__}')
    threading_example()

async def main2() -> None:
    await asyncio_example()

if __name__ == '__main__':
    main1()
    outputs = INITIAL_STATE
    asyncio.run(main2())