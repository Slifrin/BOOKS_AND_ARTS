import threading
import time
import os
import logging
import sys

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def do_smth(number:int = 0) -> int:
    n = 1
    for i in range(1_000_000):
        n *= i
    return n + number

def check_multi_t():
    threads = []
    for i in range(100):
        threads.append(threading.Thread(target=do_smth, args=[i]))
    for t in threads:
        print(f"start ---> {t}")
        t.start()

    print("#"*20, f"   {threading.active_count()}   ", "#"*20)
    for t in threading.enumerate():
        print(t)

    for t in threads:
        t.join()


def f_with_local(num):
    i = num
    name = "Jurek "
    time.sleep(1)
    print(name * i)
    print(threading.local())
    time.sleep(1)
    return name + str(i)

def check_local_data():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(f_with_local, i): i for i in range(1, 5)}
        for future in as_completed(futures):
            data = future.result()
            print(f"Data {data} from {future}")


def main():
    print(f'Hello main from : {__file__}')
    print(threading.current_thread())
    check_local_data()



if __name__ == '__main__':
    main()