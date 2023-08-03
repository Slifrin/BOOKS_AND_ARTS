import sys

def conversion_between_str_bytes():
    s = "abc"
    b = b"abc"

    assert s == b.decode()
    assert b == s.encode()

    s = "Hello str"
    b = b"Hello bytes"

    s = 'Hello str'
    b = b'Hello bytes'

    s = """Hello str"""
    b = b"""Hello bytes"""

    s = '''Hello str'''
    b = b'''Hello bytes'''

    s = "Hello str\n"
    b = b"Hello bytes\n"

    s = r"Hello str\n"
    b = rb"Hello bytes\n"

    s = f"Hello str in {__name__}"
    # b = fb"Hello bytes {__name__}" # no such thing :(


def str_bytes_functions():
    print("\nstr and bytes common functions")
    for func in sorted(set(dir(str)) & set(dir(bytes))):
        print(func)

    print("\nOnly in str")
    for func in sorted(set(dir(str)) - set(dir(bytes))):
        print(func)

    print("\nOnly in bytes")
    for func in sorted(set(dir(bytes)) - set(dir(str))):
        print(func)

def smiley():
    print()
    s = "🙂"
    print(s)
    print(len(s))
    b = s.encode()
    print(b)
    print(list(b))
    print(len(b))
    print(int.from_bytes(b, byteorder="little"))
    print(int.from_bytes(b, byteorder="big"))

    # sequence of bytes do not carry meaning they can be interpreted as we want
    # string is combined out of characters, it stores bytes interpreted as characters

    print(sys.byteorder)
    print(sys.getdefaultencoding())

def main() -> None:
    print(f'Hello main from : {__file__}')
    conversion_between_str_bytes()
    str_bytes_functions()
    smiley()


if __name__ == '__main__':
    main()