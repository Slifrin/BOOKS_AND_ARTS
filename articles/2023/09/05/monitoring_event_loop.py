"""
https://medium.com/@DorIndivo/overcoming-performance-bottlenecks-with-async-python-a-deep-dive-into-cpu-bound-code-b604a400255a
"""
import asyncio
import logging

from typing import Union

from fastapi import FastAPI

app = FastAPI()

async def monitor_event_loop_lag(loop: asyncio.AbstractEventLoop):
    start = loop.time()
    sleep_interval = 1

    while loop.is_running():
        await asyncio.sleep(sleep_interval)
        diff = loop.time() - start
        lag = diff - sleep_interval
        print(f"Info about lag {lag}")
        # send lag as a statsd metric
        if lag > 1:
            tasks = asyncio.all_tasks(loop)
            for task in tasks:
                #   if task._coro.cr_code.co_name != "monitor_event_loop_lag":
                if task.get_coro().cr_code.co_name != "monitor_event_loop_lag":
                    logging.warn(f"event loop lag:{lag}, task: {task}")
        start = loop.time()


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_running_loop()
    loop.create_task(monitor_event_loop_lag(loop))


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}