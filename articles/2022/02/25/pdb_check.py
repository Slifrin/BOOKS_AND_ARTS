"""
    https://realpython.com/python-debugging-pdb/
"""


import pdb



def main():
    print('Hello main')
    pdb.set_trace()
    print("some boring stuff")
    breakpoint()
    print("some boring stuff 2")


if __name__ == '__main__':
    main()