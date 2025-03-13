import asyncio
import sys


async def tcp_echo_client(messege):
    print('\n' + '-' * 50)
    reader, writer = await asyncio.open_connection("127.0.0.1", 9999)
    print(f"Send {messege=}")
    writer.write(messege.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received {data.decode()}")

    print("Close connection")
    writer.close()
    await writer.wait_closed()


async def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    await tcp_echo_client("Hello there\n")


if __name__ == "__main__":
    asyncio.run(main())
