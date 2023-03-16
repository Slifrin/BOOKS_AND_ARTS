import asyncio

from asyncio import StreamReader, StreamWriter

# not a gracefull way

def not_nice():
    async def f(delay):
        await asyncio.sleep(delay)

    loop = asyncio.get_event_loop()
    t1 = loop.create_task(f(1))
    t2 = loop.create_task(f(2))

    loop.run_until_complete(t1) # will run untile t1 is complite
    # Task was destroyed but it is pending!
    # task: <Task pending name='Task-2' coro=<not_nice.<locals>.f() done, defined at
    # startin_up_and_shutting_down.py:6> wait_for=<Future pending cb=[Task.task_wakeup()]>>
    loop.close()


def better_way():
    async def echo(reader: StreamReader, writer: StreamWriter):
        print("New connection")
        try:
            while data := await reader.readline():
                writer.write(data.upper())
                await writer.drain()
            print("Leaving connection")
        except asyncio.CancelledError:
            print("Connection dropped!")
    
    async def check(host='127.0.0.1', port=8888):
        server = await asyncio.start_server(echo, host, port)
        async with server:
            await server.serve_forever()

    try:
        asyncio.run(check())
    except KeyboardInterrupt:
        print("Bey!")

def better_way_with_sending_event_but_in_wrong_way():
    async def send_event(msg: str):
        await asyncio.sleep(1)
        print(f"This is a msg {msg}")
    
    async def echo(reader: StreamReader, writer: StreamWriter):
        print("New connection")
        try:
            while data := await reader.readline():
                writer.write(data.upper())
                await writer.drain()
            print("Leaving connection")
        except asyncio.CancelledError:
            msg = "Connection dropped!"
            print(msg)
            asyncio.create_task(send_event(msg))
            # As a general rule of thumb, try to avoid creating new tasks inside
            # CancelledError exception handlers. If you must, be sure to also
            # await the new task or future inside the scope of the same function.
    
    async def check(host='127.0.0.1', port=8888):
        server = await asyncio.start_server(echo, host, port)
        async with server:
            await server.serve_forever()

    try:
        asyncio.run(check())
    except KeyboardInterrupt:
        print("Bey!")

    

def main() -> None:
    print(f'Hello main from : {__file__}')
    # not_nice()
    # print("-" * 80)
    # better_way()
    print("-" * 80)
    better_way_with_sending_event_but_in_wrong_way()

if __name__ == '__main__':
    main()