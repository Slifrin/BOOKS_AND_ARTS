import asyncio
import time

async def f():
    return 123


type(f)

import inspect

print(inspect.iscoroutinefunction(f))


coro = f()
try:
    coro.send(None)
except StopIteration as e:
    print("The answer was: ", e.value)

start = time.perf_counter_ns()
async def f2():
    await asyncio.sleep(3)
    return 456
# coro2 = f2()

# coro2.send(None)

print(time.perf_counter_ns() - start)



async def f3():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("I was canceled!")
    else:
        return 789

coro3 = f3()
coro3.send(None)
try:
    coro3.throw(asyncio.CancelledError)
except StopIteration:
    print("After cancel")



async def f4():
    await asyncio.sleep(0)
    return 111

loop = asyncio.new_event_loop() # this creates a function as get_event_loop emits warning
coro4 = f4()
loop.run_until_complete(coro4)
print("After proper event loop")

