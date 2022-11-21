"""
    https://superfastpython.com/join-a-thread-in-python/
"""

import threading
from time import sleep

def joining_thread_that_has_an_error():
    def task():
        sleep(1)
        print(f"All done in new THREAD {threading.current_thread().name}")
        raise RuntimeError("Tarapaty")

    thread = threading.Thread(target=task)
    thread.start()
    print("Main thread waiting for other thred to terminate")
    thread.join()
    print("Main continiues ...")

def join_thread_with_timeout_set():
    """
        Note, the Python interpreter will only terminate when there are no non-daemon
        threads running, not when the main thread exits. The new thread we created
        is a non-daemon thread, as is the main thread.
    """
    def wait_for_thread_to_end(thread:threading.Thread):
        while True:
            if thread.is_alive():
                print("Othre thread is still running")
            else:
                print("Othre thread finished :)")
                return
            sleep(0.3)

    def task():
        sleep(5)

    thread = threading.Thread(target=task)
    thread.start()

    print("Waiting for other thread ...")
    thread.join(timeout=2)

    wait_for_thread_to_end(thread)


def main() -> None:
    print(f'Hello main from : {__file__}')
    # joining_thread_that_has_an_error()
    join_thread_with_timeout_set()

if __name__ == '__main__':
    main()