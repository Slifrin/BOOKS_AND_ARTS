import asyncio
import sys


async def handle_echo(reader, writer):
    print('\n\n' + '#' * 50)
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message} from {addr}")

    print(f"Send {message}")

    writer.write(data)
    await writer.drain()

    print(f"Close connectio to {addr}")
    writer.close()


async def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 9999)

    addr = server.sockets[0].getsockname()
    print(f"serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
