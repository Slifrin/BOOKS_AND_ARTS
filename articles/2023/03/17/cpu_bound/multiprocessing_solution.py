import multiprocessing
import time

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


def main() -> None:
    print(f'Hello main from : {__file__}')
    numbers = [5_000_000 + x for x in range(200)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration}s")


if __name__ == '__main__':
    main()