"""
    https://docs.python.org/3/library/random.html

    for security 'secrets' module should be used
"""

import random


def get_bytes():
    return random.randbytes(16)

def functions_for_ints():
    print(random.randrange(0, 10))
    print(random.randint(5, 22))
    print(random.getrandbits(8))

def functions_for_sequences():
    print(random.choice(['a', 'b', 'c']))
    print(random.shuffle([1,2,3,4]))
    print(random.sample([1,2,3,4,5,6,7,8], k=5))
    print(random.sample([1,2], counts=[4, 2], k=5))

def real_value_distributions():
    random.random()
    random.uniform(3, 5)
    random.triangular()
    # random.betavariate()
    # random.expovariate()
    # random.gammavariate()
    # random.gauss() # mu, sigma
    # random.lognormvariate()
    # random.normalvariate()
    # random.vonmisesvariate()
    # random.paretovariate()
    # random.weibullvariate()


def main():
    print(f'Hello main from : {__file__}')
    print(get_bytes())
    functions_for_ints()
    functions_for_sequences()
    real_value_distributions()

if __name__ == '__main__':
    main()