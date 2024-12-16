import sys
import time
import threading

class WorkerThread(threading.Thread):
    def run(self):
        while True:
            print('Working hard')
            time.sleep(0.5)


def main(args) -> None:
    print(f'Hello main from : {__file__}')
    use_daemon = False
    for arg in args:
        if arg == '--use_daemon':
            use_daemon = True
    worker = WorkerThread()
    worker.setDaemon(use_daemon)
    worker.start()
    time.sleep(1)
    sys.exit(0)

if __name__ == '__main__':
    potential_args = sys.argv[1:]
    # main([]) # will run forever as it waits for thread to finish
    main(['--use_daemon'])