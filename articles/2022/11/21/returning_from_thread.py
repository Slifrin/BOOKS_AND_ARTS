"""
    https://superfastpython.com/thread-return-values/

    There are two main ways to return values from a thread, they are:
        - Extend threading.Thread and store data in instance variables.
        - Store data in global variables.

    The danger of both approaches is that there could be a race condition
    between the new thread storing data in an instance variable or global
    variable and one or more other threads reading that data.

    The solution could be to protect the data with a
        threading.Lock, to use a
        threading.Event to flag that the return data is available, or to use a
        threading.Condition to notify threads that the data is ready.
    A simpler approach is to simply wait for the new thread to terminate.
"""
import threading
from random import random
from time import sleep


def return_from_thread_with_custom_thread_class():
    class CustomThread(threading.Thread):
        def __init__(self, target):
            super().__init__(target=target)
            self.new_ret_value = None

        def run(self):
            print("Running custom thread")
            sleep(1)
            self.new_ret_value = self._target()
            print(f"Got {self.new_ret_value} from target {self._target}")

    def f() -> float:
        return random()

    my_thread = CustomThread(f)
    my_thread.start()

    my_thread.join()

    print(f"MAIN thread got ret value {my_thread.new_ret_value}")

def returning_with_glogal_vars():
    """
        Very unsafe shoudl be protected with lock (mutex)
    """
    data = None
    def task():
        nonlocal data
        data = random()
        print(f"THREAD assigned value {data}")
    
    thread = threading.Thread(target=task)
    thread.start()
    thread.join()
    print(f"Main THREAD got {data}")

def main() -> None:
    print(f'Hello main from : {__file__}')
    return_from_thread_with_custom_thread_class()
    returning_with_glogal_vars()

if __name__ == '__main__':
    main()