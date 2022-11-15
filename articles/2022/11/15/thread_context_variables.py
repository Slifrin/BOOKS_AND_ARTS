"""
    https://superfastpython.com/thread-context-variables-in-python/
"""

import time
import random
import threading
import contextvars

COLOR = 'Unknown'
COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

context_color = contextvars.ContextVar('color', default='Unknown')

def color_reporter():
    global COLOR
    time.sleep(random.random())
    print(f"the colot is {COLOR}")

def context_color_reporter():
    global context_color
    time.sleep(random.random())
    print(f"the colot is {context_color.get()}")

def process_colors():
    for col in COLORS:
        global COLOR
        COLOR = col
        color_reporter()

def task(color_arg):
    global COLOR
    COLOR = color_arg
    color_reporter()

def context_task(color_arg):
    global context_color
    context_color.set(color_arg)
    context_color_reporter()

def naive_usage_of_globals_with_threads():
    """
    All colors report purple as it is last asigned value.
    """
    threads = [threading.Thread(target=task, args=(color, )) for color in COLORS]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def context_usage_of_globals_with_threads():
    """
    All colors report purple as it is last asigned value.
    """
    threads = [threading.Thread(target=context_task, args=(color, )) for color in COLORS]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def main() -> None:
    print(f'Hello main from : {__file__}')
    # process_colors()
    # naive_usage_of_globals_with_threads()
    context_usage_of_globals_with_threads()



if __name__ == '__main__':
    main()