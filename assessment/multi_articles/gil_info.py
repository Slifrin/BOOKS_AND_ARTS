"""
https://realpython.com/python-gil/
"""

from threading import Thread
from multiprocessing import Pool

import sys
import time


def cpu_bound():
    COUNT = 50_000_000

    def countdown(n):
        while n > 0:
            n -= 1

    start = time.time()
    countdown(COUNT)
    end = time.time()

    print(f"Time taken in secounds - {end - start}")

    start = time.time()
    tasks = []
    n = 2
    for _ in range(n):
        task = Thread(target=countdown(COUNT // n))
        task.start()
        tasks.append(task)

    for task in tasks:
        task.join()

    end = time.time()
    print(f"Time taken in secounds - {end - start}")

    start = time.time()
    with Pool(processes=n) as pool:
        processes = []
        for _ in range(n):
            processes.append(pool.apply_async(countdown, [COUNT // n]))
    end = time.time()
    print(f"Time taken in secounds - {end - start}")


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    a = []
    b = a
    print(sys.getrefcount(a))

    cpu_bound()
    print(sys.getswitchinterval())


if __name__ == "__main__":
    main()
