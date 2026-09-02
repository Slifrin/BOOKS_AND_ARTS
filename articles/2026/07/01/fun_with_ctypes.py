import ctypes
import ctypes.util
import sys




def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    for e in dir(ctypes):
        print(e)

if __name__ == '__main__':
    main()