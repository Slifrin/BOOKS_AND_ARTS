"""
    https://superfastpython.com/threading-in-python/

    When we create and run a new thread, Python will make system calls on the
    underlying operating system and request a new thread be created and to start
    running the new thread.

    This highlights that Python threads are real threads,
    as opposed to simulated software threads, e.g. fibers or green threads.

    Concurrent: Code that can be executed out of order.
    Parallel: Capability to execute code simultaneously.

    ABOUT GIL
    Such as when the thread is blocked, such as performing IO with a socket or file,
    or often if the thread is executing computationally intensive code in a C library, like hashing bytes.

    Luckily, many potentially blocking or long-running operations, such as I/O, image processing,
    and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs
    that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck.


    Additionally, the Python interpreter will release the GIL when performing blocking IO operations,
    allowing other threads within the Python process to execute.

    Therefore, blocking IO provides an excellent use case for using threads in Python.

    Examples of blocking IO operations include:

        Reading or writing a file from the hard drive.
        Reading or writing to standard output, input or error (stdin, stdout, stderr).
        Printing a document.
        Reading or writing bytes on a socket connection with a server.
        Downloading or uploading a file.
        Querying a server.
        Querying a database.
        Taking a photo or recording a video.
        And so much more

    !!! A blocking call is a function call that does not return until it is complete. !!!
    Blocking Calls on Concurrency Primitives like:
        Waiting for a lock, e.g. calling acquire() on a threading.Lock.
        Waiting to be notified, e.g. calling wait() on a threading.Condition.
        Waiting for a thread to terminate, e.g. calling join() on a threading.Thread.
        Waiting for a semaphore, e.g. calling acquire() on a threading.Semaphore.
        Waiting for an event, e.g. calling wait() on a threading.Event.
        Waiting for a barrier, e.g. calling wait() on a threading.Barrier.
    Blocking Calls for I/O
        Hard disk drive: Reading, writing, appending, renaming, deleting, etc. files.
        Peripherals: mouse, keyboard, screen, printer, serial, camera, etc.
        Internet: Downloading and uploading files, getting a webpage, querying RSS, etc.
        Database: Select, update, delete, etc. SQL queries.
        Email: Send mail, receive mail, query inbox, etc.

    Thread Reentrant Lock
        it can be acquired more than once by !!!SAME!!! but eache time it needs to release it
    
    Thread Semaphore:
        A semaphore is a concurrency primitive that allows a limit on the number of threads
        that can acquire a lock protecting a critical section.
    A semaphore provides a useful concurrency tool for limiting the number of threads
    that can access a resource concurrently. Some examples include:
        Limiting concurrent socket connections to a server.
        Limiting concurrent file operations on a hard drive.
        Limiting concurrent calculations.

    event is a thread-safe boolean flag.

    Barrier
    It allows multiple threads to wait on the same barrier object instance (e.g. at the same
    point in code) until a predefined fixed number of threads arrive (e.g. the barrier is full),
    after which all threads are then notified and released to continue their execution.
    Internally, a barrier maintains a count of the number of threads waiting on the barrier
    and a configured maximum number of parties (threads) that are expected. Once the expected
    number of parties reaches the pre-defined maximum, all waiting threads are notified.

"""

from threading import Thread, current_thread, main_thread, active_count, get_ident, get_native_id, enumerate, excepthook, Condition, Semaphore, Event, Timer, Barrier
from threading import BrokenBarrierError
from time import sleep
from random import random

def check_info_about_thread():
    thread = Thread(target=lambda: sleep(1))

    print(f"{thread.name} {thread.native_id}")
    thread.start()
    print(f"Number of active threads = {active_count()}")
    print(f"{thread.name=} {thread.native_id=} {thread.daemon=} {thread.is_alive()}")
    print(current_thread())
    print(main_thread())
    print(get_ident())
    print(get_native_id()) # id assigned to thread by OS

    for t in enumerate():
        print(t)

    thread.join()


def check_condition():
    def task(condition:Condition, work_list: list):
        sleep(1)
        work_list.append(33)
        print(f"Task sends notification from {current_thread()}")
        with condition:
            condition.notify()

    condition = Condition()
    work_list = list()

    print("Waiting for condition")
    with condition:
        worker = Thread(target=task, args=(condition, work_list))
        worker.start()
        condition.wait()
    print(f"Got data {work_list}")

def check_semaphore():
    def task(semaphore: Semaphore, number: float):
        with semaphore:
            value = random()
            sleep(value)
            print(f"Thread number {number}, got value {value}")

    semaphore = Semaphore(2)
    for i in range(10):
        worker = Thread(target=task, args=(semaphore, i))
        worker.start()
    sleep(3)

def check_barrier():
    def task(barrier, number):
        value = random() * 10
        sleep(value)
        print(f"Thread number {number} done, got: {value}")
        barrier.wait()
        print(f"AFTER WAIT -- Thread number {number}")

    def callback():
        print("required numbre of threads finished".upper())

    print("Hello Barriers")
    barrier = Barrier(5 + 1, action=callback, timeout=15) # barrier waits for given number of tasks and it is required that all of them finish
    threads: list[Thread] = []
    for i in range(20):
        worker = Thread(target=task, args=(barrier, i))
        worker.start()
        threads.append(worker)
    print("Main thread waits for all results")
    barrier.wait()
    print("All threads have their result ")
    for t in threads:
        name = t.name
        print("THREAD info ------> ", t.name, t.is_alive())

        try:
            t.join()
        except BrokenBarrierError as e:
            # Exception is in thread itself not in join execution 
            print("HMMM some kind of trouble in thread {name}")
            print(str(e))

    for t in threads:
        print(t.name, t.is_alive())
    print("Hello after join")
    # print("Need to abrt barrier")
    # barrier.abort()
    # print("AFTER ABORT")

def main() -> None:
    print(f'Hello main from : {__file__}')
    # check_info_about_thread()
    # check_condition()
    # check_semaphore()
    try:
        check_barrier()
    except Exception as e:
        print(f"\n\nGot EXCEPTION in outer scope\n")
        print(str(e))
        print("\n\n\n")

if __name__ == '__main__':
    main()