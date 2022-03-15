"""
    https://docs.python.org/3/library/fileinput.html#module-fileinput

    http://pymotw.com/3/fileinput/
"""


import fileinput

for line in fileinput.input(files=('spr1.txt', 'spr2.txt'), encoding='utf-8'):
    print(line)