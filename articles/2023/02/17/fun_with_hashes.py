import hashlib
import hmac
import io


from pprint import pprint


def sign_cookis_and_compare_theme():
    SECRET_KEY = b'pseudorandomly generated server secret key'
    AUTH_SIZE = 16

    def sign(cookie):
        h = hashlib.blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
        h.update(cookie)
        return h.hexdigest().encode('utf-8')

    def verify(cookie, sig):
        good_sign = sign(cookie)
        return hmac.compare_digest(good_sign, sig)

    cookie = b'user-bob'
    sig = sign(cookie)
    print("{0},{1}".format(cookie.decode('utf-8'), sig))

    print(verify(cookie, sig))
    print(verify(b'user-john', sig))


def example2():
    """
    new in python 3.11
    with open(hashlib.__file__, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        print(digest.hexdigest())
    """

def example1():
    print(hashlib.algorithms_guaranteed)
    print(hashlib.algorithms_available)

    m = hashlib.sha256()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    print(m.digest_size)
    pprint(dir(m))
    print(m.digest())
    print(m.hexdigest())

def main() -> None:
    print(f'Hello main from : {__file__}')
    sign_cookis_and_compare_theme()


if __name__ == '__main__':
    main()