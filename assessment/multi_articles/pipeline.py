import logging
import threading
import queue


class Pipeline:
    def __init__(self) -> None:
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()

        logging.debug("%s:have getlock", name)
        message = self.message

        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()

        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()

        logging.debug("%s:have setlock", name)
        self.message = message

        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()

        logging.debug("%s:getlock released", name)


class QPipeline(queue.Queue):
    def __init__(self, maxsize: int = 100) -> None:
        super().__init__(maxsize)
    
    def get_message(self, name):
        logging.debug("%s:about to get from queue", name)
        value = self.get()
        logging.debug("%s: got %d from queue", name, value)
        return value
    
    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s: added %d to queue", name, value)
