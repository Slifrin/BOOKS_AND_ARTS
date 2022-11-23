"""
    https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

    - Raising exceptions in a python thread
    - Set/Reset stop flag
    - Using traces to kill threads
    - Using the multiprocessing module to kill threads
    - Killing Python thread by setting it as daemon
    - Using a hidden function _stop()
"""
import sys
import threading
import ctypes
import time
import trace

def raising_exceptio_in_thread():
    class ThreadWithExceptio(threading.Thread):
        def __init__(self, name):
            super().__init__()
            self._name = name
        
        def run(self):
            try:
                while True:
                    print(f"Running {self.name}")
                    time.sleep(0.5)
            finally:
                print("THIS IS THE END")
        
        def get_id(self):
            if hasattr(self, '_thread_id'):
                return self.ident
            for thread in threading.enumerate():
                if thread is self:
                    return threading.get_ident()

        def raise_exceptio(self):
            # thread_id = self.ident
            # thread_id = threading.get_ident()
            thread_id = self.native_id
            print('Infom  about ID', thread_id)
            # need to investigate the function call
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))

            if res > 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                print('Exception raise failure')


    t1 = ThreadWithExceptio("My_NAME")
    t1.start()
    time.sleep(2)
    t1.raise_exceptio()
    t1.join()

def set_reset_stop_flag():

    def run(stop):
        while True:
            print('thread running')
            time.sleep(0.1)
            if stop(): # It is nice to call passed function
                    break

    stop_threads = False
    t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
    t1.start()
    time.sleep(1)
    stop_threads = True
    t1.join()
    print('thread killed')


def using_traces_to_kill_threads():
    
    class ThreadWithTrace(threading.Thread):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.killed = False
        
        def start(self):
            self.__run_backup = self.run
            self.run = self.__run
            super().start()
        
        def __run(self):
            sys.settrace(self.globaltrace)
            self.__run_backup()
            self.run = self.__run_backup

        def globaltrace(self, frame, event, arg):
            if event == 'call':
                return self.localtrace
            else:
                return None
            
        def localtrace(self, frame, event, arg):
            if self.killed:
                if event == 'line':
                    raise SystemExit()
            return self.localtrace
        
        def kill(self):
            self.killed = True

    def func():
        while True:
            print('Thread is running')
            time.sleep(0.2)

    t1 = ThreadWithTrace(target=func)
    t1.start()
    time.sleep(2)
    t1.kill()
    t1.join()
    if not t1.is_alive():
        print("thread killed")
    print('After check')

def main() -> None:
    print(f'Hello main from : {__file__}')
    # raising_exceptio_in_thread()
    # set_reset_stop_flag()
    using_traces_to_kill_threads()

if __name__ == '__main__':
    main()