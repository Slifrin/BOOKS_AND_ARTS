import secrets
import string
import sys


def generate_simple_secret():
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(16))
    print(password)

def main() -> None:
    print(f'Hello main from : {__file__} executed by {sys.executable}')
    generate_simple_secret()


if __name__ == '__main__':
    main()