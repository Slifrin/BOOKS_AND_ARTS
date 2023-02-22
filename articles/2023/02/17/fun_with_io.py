import io
import os
import sys
import locale


def main() -> None:
    print(f'Hello main from : {__file__}')
    print(os.getcwd())
    print(locale.getdefaultlocale())
    print(io.DEFAULT_BUFFER_SIZE)

    # with open("myfile.txt", "wb") as f:
    #     f.write(b"hello there")
    some_bytes = b'\xC3\xA9'
    print(some_bytes, len(some_bytes)) # b'\xc3\xa9' 2
    print(some_bytes.decode()) # é

    with open("myfile_b.txt", "wb") as f:
        f.write(some_bytes)
        f.write(hex(123).encode('utf8'))

    arr = [65,66,67,68]
    some_bytes = bytearray(arr)

    some_bytes.append(42)

    immutable_bytes = bytes(some_bytes)
    print(some_bytes)
    print(immutable_bytes)
    print(immutable_bytes.decode())

    with open("data.dat", "r") as f:
        print(f.read())

    print('Hello 🙂 hello 🔥 there'.encode())

if __name__ == '__main__':
    main()