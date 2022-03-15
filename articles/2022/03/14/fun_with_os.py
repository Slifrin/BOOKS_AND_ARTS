"""
    https://docs.python.org/3/library/os.html
"""

import os
import sys



def main():
    print(f'Hello main from : {__file__}')
    print(os.name)
    print(sys.getfilesystemencoding())
    print(os.fspath('.'))

    print(os.getgid())
    print(os.getegid())

    print(os.getgroups())

    print(os.getpid())

    print("check os.scandir")
    # https://docs.python.org/3/library/os.html#os.DirEntry
    with os.scandir("/Users/Jerzy_Kiedrowski/Desktop/NAUKA/py_fun/books_and_arts/articles/2022/03") as it:
        for entry in it:
            # if not entry.name.startswith('.') and entry.is_file():
            print(entry.name, entry.is_dir(), entry.is_file())
    # pid, fd = os.forkpty()
    input("some input: ")

if __name__ == '__main__':
    main()