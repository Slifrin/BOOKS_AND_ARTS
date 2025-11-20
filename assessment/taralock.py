import threading

import sys
import time
import concurrent.futures

def update_data1(l: list, lock: threading.Lock):
    with lock:
        var = l[-1]
        time.sleep(0.1)
        var += 2
        l[-1] = var

def update_data2(l: list):
    var = l[-1]
    time.sleep(0.1)
    var += 5
    l[-1] = var



def main() -> None:
    """All elements need to lock"""
    print(f'Hello main from : {__file__} executed by {sys.executable}')

    lock = threading.Lock()

    for _ in range(10):
        dummy = [1, 1]
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(update_data2, dummy)
            executor.submit(update_data1, dummy, lock)

        print(dummy)


if __name__ == '__main__':
    main()