import os

try:
    with open("counterfile") as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def sevecounter():
    with open("counterfile", "w") as outfile:
        outfile.write('%d' % _count)


def goodbay(name, adjective):
    print(f"Goodbye {name}, it was {adjective} to meet you.")

import atexit

atexit.register(sevecounter)
atexit.register(goodbay, "Donny", "nice")
atexit.register(goodbay, adjective="nice", name="Donny")

@atexit.register
def say_goodbye():
    print(f"Good by this python {os.getpid()} {os.getlogin()}")
    print(os.uname(), os.ctermid())