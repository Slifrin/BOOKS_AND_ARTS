import base64


def check_base():
    print(base64.b64encode(b"hello there"))
    print(base64.standard_b64encode(b"hello there"))
    print(base64.urlsafe_b64encode(b"hello there"))
    print(base64.b32encode(b"hello there"))



def main() -> None:
    print(f'Hello main from : {__file__}')
    check_base()

if __name__ == '__main__':
    main()