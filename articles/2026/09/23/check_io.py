import io
import os
import sys


def text_io():
    f = io.StringIO("some initial text")
    print(f.tell())


def bytes_io():
    f = io.BytesIO(b"some initial binary data: \x00\x01")
    print(f.tell())
    ba = bytearray(100)

    f.readinto(ba)
    print(ba)

    b = bytes()
    try:
        f.readinto(b)
    except TypeError as err:
        print(err)

    print(f.getbuffer())
    print(f.getvalue())

def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    print(f"{os.SEEK_SET}")
    print(f"{os.SEEK_CUR}")
    print(f"{os.SEEK_END}")
    text_io()
    bytes_io()

if __name__ == '__main__':
    main()