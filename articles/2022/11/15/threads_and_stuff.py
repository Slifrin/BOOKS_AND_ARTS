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
"""

from threading import Thread, current_thread, main_thread, active_count, get_ident, get_native_id, enumerate, excepthook
from time import sleep

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


def main() -> None:
    print(f'Hello main from : {__file__}')
    check_info_about_thread()

if __name__ == '__main__':
    main()