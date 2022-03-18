"""
https://www.python-engineer.com/posts/inplace-file-editing/
"""

import fileinput
import os
"""
Note that the input filenames aren't specified in the above program. Instead, you'll pass them as command line arguments
python3 articles/2022/02/21/in_place_file_editing.py articles/2022/02/21/sample_files/*.txt
"""

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'sample_files')


def case1():
    with fileinput.input(inplace=True) as f:
        for ip_line in f:
            op_line = ip_line.replace('/programs/', '/bin/')
            print(op_line, end='')


def case2():

    ip_files = (
        os.path.join(SAMPLES_DIR, i) for i in ['notes.txt', 'tools.txt'])

    with fileinput.input(files=ip_files, inplace=True) as f:
        for ip_line in f:
            op_line = ip_line.replace('/bin/', '/programs/')
            print(op_line, end='')


def case3():
    colors_f = os.path.join(SAMPLES_DIR, 'colors.txt')
    with fileinput.input(files=colors_f, inplace=True, backup='.orig') as f:
        for ip_line in f:
            op_line = ip_line.replace('blue', 'brown')
            print(op_line, end='')


def main():
    print('Hello main')
    case3()


if __name__ == '__main__':
    main()