"""
    https://docs.python.org/3/library/secrets.html#module-secrets
"""

import secrets
import string


def random_numbers_fun():
    print(f"Runnong {random_numbers_fun.__name__}")
    s_numbers = secrets.SystemRandom()
    print(dir(s_numbers))
    print(s_numbers.random())
    print(s_numbers.randint(10, 20))

    print(secrets.choice(["Witam", "Hello", "Hi"]))

    print(secrets.randbelow(100))

    print(secrets.randbits(8))


def token_generation():
    print(f"Runnong {token_generation.__name__}")

    print(secrets.token_bytes(16))

    print(secrets.token_hex(16))

    print(secrets.token_urlsafe(16))


def recipes_and_best_practices():
    print(f"Runnong {recipes_and_best_practices.__name__}")

    # Generate an eight-character alphanumeric password:
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(8))
    print(password)
    """
        Generate a ten-character alphanumeric password with at least one lowercase character,
        at least one uppercase character, and at least three digits:
    """
    password = ""
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(10))
        if (
            (any(c.islower()) for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
        ):
            break
    print(password)

    # Generate an XKCD-style passphrase:
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        password = "_".join(secrets.choice(words) for i in range(5))
        print(password)

    # Generate a hard-to-guess temporary URL containing a security token suitable for password recovery applications
    url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
    print(url)

def main():
    print(f"Hello main from : {__file__}")
    random_numbers_fun()
    token_generation()
    recipes_and_best_practices()


if __name__ == "__main__":
    main()
