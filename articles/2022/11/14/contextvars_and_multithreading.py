"""
    https://kobybass.medium.com/python-contextvars-and-multithreading-faa33dbe953d
"""

import contextlib
import contextvars
import time

from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed

current_user = contextvars.ContextVar("Name of current user")

def print_hello():
    print(f"Hello, {current_user.get()}")

def handel_request(user):
    current_user.set(user)
    print_hello()

def check_with_thread():
    Thread(target=handel_request, args=("Koby",)).start()
    Thread(target=handel_request, args=("World",)).start()

def say_hello():
    time.sleep(1)
    return "Hello user"

def offer_sympathies():
    time.sleep(1)
    return "Very sorry, user"


def check_thread_pool():
    with ThreadPoolExecutor() as exec:
        tasks = (say_hello, offer_sympathies)
        futures = (exec.submit(task) for task in tasks)
        for future in as_completed(futures):
            print(future.result())

def say_hello_2():
    time.sleep(1)
    return f"Hello, {current_user.get()}"

def offer_sympathies_2():
    time.sleep(1)
    return f"Very sorry, {current_user.get()}"

def executor_and_contextvars():
    current_user.set("Tom")
    with ThreadPoolExecutor() as exec:
        tasks = (say_hello_2, offer_sympathies_2)
        futures = (exec.submit(task) for task in tasks)
        for future in as_completed(futures):
            print(future.result())

# to ceorrect this problem with executor

def set_context(context):
    """ It is calld with copy of context set_context(contextvars.copy_context()) """
    print(context, dir(context))
    for var, value in context.items():
        var.set(value)

def correct_executor_end_context_vars():
    current_user.set("Tom")
    parent_context = contextvars.copy_context()
    with ThreadPoolExecutor(initializer=set_context, initargs=(parent_context, )) as exec:
        tasks = (say_hello_2, offer_sympathies_2)
        futures = (exec.submit(task) for task in tasks)
        for future in as_completed(futures):
            print(future.result())

# Other option is to create subclass which will handle some steps automaticly
class ContextExecutor(ThreadPoolExecutor):
    def __init__(self):
        self.context = contextvars.copy_context()
        super().__init__(initializer=self._set_child_context)
    
    def _set_child_context(self):
        for var, value in self.context.items():
            var.set(value)

def cunstom_executor():
    current_user.set("Bob")
    parent_context = contextvars.copy_context()
    with ContextExecutor() as exec:
        tasks = (say_hello_2, offer_sympathies_2)
        futures = (exec.submit(task) for task in tasks)
        for future in as_completed(futures):
            print(future.result())

# More functional approach (wrapper function)
@contextlib.contextmanager
def ContextExecutor_but_wrapped():
    parent_context = contextvars.copy_context()
    with ThreadPoolExecutor(initializer=set_context, initargs=(parent_context, )) as executor:
        yield executor

def cunstom_executor_with_functional_approuch():
    current_user.set("Johny")
    with ContextExecutor_but_wrapped() as exec:
        tasks = (say_hello_2, offer_sympathies_2)
        futures = (exec.submit(task) for task in tasks)
        for future in as_completed(futures):
            print(future.result())


def main() -> None:
    print(f'Hello main from : {__file__}')
    # check_with_thread()
    # check_thread_pool()
    # executor_and_contextvars() # LookupError: <ContextVar name='Name of current user' at 0x7fb1f422a360>
    correct_executor_end_context_vars()
    cunstom_executor()
    cunstom_executor_with_functional_approuch()


if __name__ == '__main__':
    main()