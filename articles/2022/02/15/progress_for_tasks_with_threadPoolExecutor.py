"""
https://superfastpython.com/threadpoolexecutor-progress/
"""
import sys

from concurrent.futures import ThreadPoolExecutor, Future, wait
from typing import Awaitable
from time import sleep
from random import random
from threading import Lock


lock = Lock()
tasks_total = 20
tasks_completed = 0


def progress_indicator(future):
    global lock, tasks_total, tasks_completed
    with lock:
        tasks_completed += 1
        msg = f'{tasks_completed}/{tasks_total} completed, {tasks_total-tasks_completed} remain.'
        sys.stdout.write('\x08' * (len(msg) + 1))
        print(msg, end='')
        sys.stdout.flush()
    sys.stdout.write(' ' * len(msg) + '\x08' * len(msg))


def custom_callback(future : Future):
    if future.cancelled():
        print("Canceled : ", future)
    if future.exception():
        print("Canceled : ", future, future.exception())
    else:
        # print("Successfully finished ", future)
        print('.', end='', flush=True)


def task(name):
    sleep(random())

def main():
    print('Hello main')
    with ThreadPoolExecutor(2) as executor:
        futures = [executor.submit(task, i) for i in range(20)]
        for future in futures:
            future.add_done_callback(progress_indicator)
        sys.stdout.flush()        

if __name__ == '__main__':
    main()