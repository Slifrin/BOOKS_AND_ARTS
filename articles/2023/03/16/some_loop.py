import asyncio
import random



colors = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)



async def makerandom(idx: int, threshold: int = 6) -> int:
    print(colors[idx + 1] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(colors[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(colors[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + colors[0])
    return i


async def main():
    print(f'Hello main from : {__file__}')
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == '__main__':
    random.seed(2137)
    values = asyncio.run(main())
    print()
    for i, val in enumerate(values):
        print(f"value {i} ---> {val}")
    