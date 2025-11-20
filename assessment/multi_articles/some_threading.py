"""
https://realpython.com/intro-to-python-threading/
"""

import logging
import sys
import threading
import time
import concurrent.futures


def thread_function(name):
    logging.info(f"Thread {name}: starting.")

    time.sleep(2)

    logging.info(f"Thread {name}: finishing.")


def usage_of_one_thread():
    logging.info("Main     : before creating thred")
    x = threading.Thread(target=thread_function, args=(1,))
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main     : before running thred")
    x.start()
    logging.info("Main     : wait for thread for finish")
    x.join()
    logging.info("Main     : all done")


def using_multiple_threads(threads_number=3):
    threads = []

    for index in range(threads_number):
        logging.info("Main     : before creating and starting thred %d.", index)
        t = threading.Thread(target=thread_function, args=(index,))
        threads.append(t)
        t.start()

    for index, t in enumerate(threads):
        logging.info("Main     : before joining thred %d.", index)
        t.join()
        logging.info("Main     : thread %d done.", index)

    logging.info("Main     : all done")


def using_pool():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))


def race_conditions():
    class FakeDatabase:
        def __init__(self):
            self.value = 0
        def update(self, name):
            logging.info("Thread %s: starting update", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info("Thread %s: finishing update.", name)

    class FakeDatabaseWithLock:
        def __init__(self):
            self.value = 0
            self._lock = threading.Lock()
        def update(self, name):
            logging.info("Thread %s: starting update", name)
            logging.debug("Thread %s: about to lock", name)
            with self._lock:
                local_copy = self.value
                local_copy += 1
                time.sleep(0.1)
                self.value = local_copy
                logging.debug("Thread %s: about to release lock.", name)
            
            logging.debug("Thread %s: after release.", name)
            logging.info("Thread %s: finishing update.", name)

    def race():
        database = FakeDatabase()
        logging.info("Testing update. Starting value is %d", database.value)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            for index in range(2):
                executor.submit(database.update, index)

        logging.info("Testing update. Ending value is %d", database.value)

    def no_race():
        database = FakeDatabaseWithLock()
        logging.info("Testing update. Starting value is %d", database.value)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            for index in range(2):
                executor.submit(database.update, index)

        logging.info("Testing update. Ending value is %d", database.value)

    race()
    no_race()


def deadlock():
    l = threading.Lock()
    print("Befor first acquire")
    l.acquire()
    print("Befor second acquire")
    l.acquire()
    print("Acquired lock TWICE!!!!")
    """
The design issue can be a bit trickier in some languages.
Thankfully, Python threading has a second object, called RLock, that is designed
for just this situation. It allows a thread to .acquire() an RLock multiple
times before it calls .release(). That thread is still required to call .release()
the same number of times it called .acquire(), but it should be doing that anyway
    """


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    format = "%(asctime)s: %(message)s"
    logging_level = logging.DEBUG
    logging.basicConfig(format=format, level=logging_level, datefmt="%H:%M:%S")

    # usage_of_one_thread()
    # using_multiple_threads()
    # using_pool()
    race_conditions()

if __name__ == "__main__":
    main()
