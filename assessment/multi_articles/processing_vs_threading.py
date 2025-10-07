"""
https://engineering.contentsquare.com/2018/multithreading-vs-multiprocessing-in-python/
"""

import sys
import multiprocessing
import threading
import concurrent.futures
import time
import logging
import os
import functools


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        start = time.perf_counter()
        ret_val = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Call to {func.__name__} took {end - start:,.2f}")

        return ret_val

    return wrapper


def cpu_task(x):
    print("I am", x)
    count = 0
    for i in range(10**8):
        count += i


@measure_time
def multi_t(func, args, workers):
    with concurrent.futures.ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)

    return list(res)


@measure_time
def multi_p(func, args, workers):
    with concurrent.futures.ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)

    return list(res)


def check_cpu_heavy():
    number_of_workers = 12

    multi_t(cpu_task, range(number_of_workers), number_of_workers)

    multi_p(cpu_task, range(number_of_workers), number_of_workers)


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    check_cpu_heavy()


if __name__ == "__main__":
    main()
