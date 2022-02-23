import unicodedata
import sys

def get_char_info(name):
    print(f"Searching for characters containning '{name}' in them")

    for i in range(sys.maxunicode):
        c = chr(i)
        
        c_name = unicodedata.name(c, "No niestery nie ma takiego imienia")
        if name in c_name:
            print('{#10+} {!r}'.format(c, c_name))


def main():
    get_char_info('sun')

if __name__ == '__main__':
    main()