"""
    https://docs.python.org/3/library/hashlib.html
"""

import hashlib

def first_experiment():
    m = hashlib.sha256()
    m.update(b"Nobody inspects")
    m.update(b" the spammish repetition")
    print(m.digest())
    print(m.hexdigest())

def main() -> None:
    print(f'Hello main from : {__file__}')
    first_experiment()

if __name__ == '__main__':
    main()