import mmap
import os
import time

from multiprocessing import Process
from multiprocessing import shared_memory

def from_documentation():
    f_name = 'tmp_file.txt'

    with open(f_name, 'wb') as f:
        f.write(b"Hello Python!\n")

    with open(f_name, 'r+b') as f:
        # memory-map the file, size 0 means whole file
        mm = mmap.mmap(f.fileno(), 0)

        # read content via standard file methods
        print(mm.readline())

        # read content via slice notation
        print(mm[:5])
        # update content using slice notation;
        # note that new content must have same size
        mm[6:] = b" World!\n"
        # ... and read again using standard file methods
        mm.seek(0)
        print(mm.readline())
        # close the map
        mm.close()

def anonymous_map_to_exchange_data_between_parent_and_child_processes():
    mm = mmap.mmap(-1, 13)
    mm.write(b"Hello World!")

    pid = os.fork()

    if pid == 0:
        mm.seek(0)
        print(mm.readline())
        
        mm.close()

# anonymous_map_to_exchange_data_between_parent_and_child_processes()

"""
    https://realpython.com/python-mmap/

    Python’s mmap uses shared memory to efficiently share large
    amounts of data between multiple Python processes, threads, and tasks
    that are happening concurrently.
"""


def regular_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        text = file_obj.read()
        print(text[:20])
        # print(text)


def mmap_io(filename):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
            print(text[:20])
            # print(text)

def check_donQuixote():
    regular_io('donQuixote.txt')
    mmap_io('donQuixote.txt')

def sharing_with_mmap():
    BUF = mmap.mmap(-1, length=100, access=mmap.ACCESS_WRITE)

    pid = os.fork()
    if pid == 0:
        # Child process
        BUF[0:100] = b"a" * 100
    else:
        time.sleep(2)
        print(BUF[0:100])

# check_donQuixote()
# sharing_with_mmap()

"""
    Here, you attempt to create a new process and pass it the memory-mapped buffer.
    This code will immediately raise a TypeError because the mmap object can’t be pickled,
    which is required to pass the data to the second process. So, to share data
    with memory mapping, you’ll need to stick to the lower-level os.fork().

    If you’re using Python 3.8 or newer, then you can use the new shared_memory
    module to more effectively share data across Python processes:
"""

def modify(buf_name):
    shm = shared_memory.SharedMemory(buf_name)
    shm.buf[0:50] = b"b" * 50
    shm.close()


def main():
    print(f'Hello main from : {__file__}')

if __name__ == '__main__':
    main()

    shm = shared_memory.SharedMemory(create=True, size=100)

    try:
        shm.buf[0:100] = b"a" * 100
        proc = Process(target=modify, args=(shm.name,))
        proc.start()
        proc.join()
        print(bytes(shm.buf[:100]))
    finally:
        shm.close()
        shm.unlink()