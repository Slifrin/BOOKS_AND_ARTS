"""
    https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/?tab=article
"""
import multiprocessing
import time


def func(number):
    for i in range(1, 10):
        time.sleep(0.2)
        print(f"Process {number} : prints {i * number}")


def main() -> None:
    print(f'Hello main from : {__file__}')

    processes = []
    for i in range(1, 4):
        process = multiprocessing.Process(target=func, args=(i, ))
        process.start()
        processes.append(process)

    print("Before killing")
    time.sleep(1)
    for proc in processes:
        proc.terminate()
    print("After termiantion")

if __name__ == '__main__':
    main()