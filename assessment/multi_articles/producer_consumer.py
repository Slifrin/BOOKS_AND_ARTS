import random
import sys
import logging
import concurrent.futures
import threading
import time
import queue

from functools import partial

from pipeline import Pipeline, QPipeline


SENTINEL = object()


def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s_%d", message, index)
        pipeline.set_message(message, "Producer")

    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipline.get_message("Consumer")

        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)


def basic_example():
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)


def q_producer(pipeline, event: threading.Event):
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")
    logging.info("Producer received EXIT event. Exiting")


def q_consumer(pipeline, event: threading.Event):
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )
    logging.info("Consumer received EXIT event. Exiting")


def q_example():
    pipeline = QPipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(q_producer, pipeline, event)
        executor.submit(q_consumer, pipeline, event)

        time.sleep(0.0001)
        logging.info("Main: about to set event")
        event.set()


def direct_queue():
    def direct_producer(queue, event):
        while not event.is_set():
            message = random.randint(1, 101)
            logging.info("Producer got message: %s", message)
            queue.put(message)

        logging.info("Producer received event. Exiting")

    def direct_consumer(queue, event):
        while not event.is_set() or not queue.empty():
            message = queue.get()
            logging.info(
                "Consumer storing message: %s (size=%d)", message, queue.qsize()
            )

        logging.info("Consumer received events. Exiting")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executro:
        executro.submit(direct_producer, pipeline, event)
        executro.submit(direct_consumer, pipeline, event)

        time.sleep(0.0001)
        logging.info("Main: about to set event")
        event.set()


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")

    format = "%(asctime)s: %(message)s"
    logging_level = logging.INFO
    logging.basicConfig(format=format, level=logging_level, datefmt="%H:%M:%S")

    # basic_example()
    # q_example()
    # direct_queue()

    some_method = partial(print, "Hello")

    # Useful primitives
    threading.Semaphore()

    some_timer = threading.Timer(1.0, some_method)
    some_timer.start()
    time.sleep(2)

    threading.Barrier(parties=3)
"""
A threading.Barrier can be used to keep a fixed number of threads in sync.
When creating a Barrier, the caller must specify how many threads will be
synchronizing on it. Each thread calls .wait() on the Barrier.
They all will remain blocked until the specified number of threads are
waiting, and then the are all released at the same time.

One use for a Barrier is to allow a pool of threads to initialize themselves.
Having the threads wait on a Barrier after they are initialized will ensure
that none of the threads start running before all of the threads are
finished with their initialization.
"""

if __name__ == "__main__":
    main()
